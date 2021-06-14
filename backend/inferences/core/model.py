import os
import glob

import cv2
import numpy as np
from PIL import Image

import SimpleITK as sitk
from lungmask import mask as msk
from skimage import measure

from tensorflow import keras
from tensorflow.keras import backend as K
from tensorflow.keras.models import load_model

from scipy.ndimage import gaussian_filter as gf
from scipy.ndimage.morphology import binary_dilation

MODEL_PATH = f'{os.getcwd()}/inferences/core/h5s/model.h5'
WEIGHTS_0_PATH = f'{os.getcwd()}/inferences/core/h5s/weight_0.h5'
WEIGHTS_1_PATH = f'{os.getcwd()}/inferences/core/h5s/weight_1.h5'

BATCH_SIZE = 16


class Model:
    def __init__(self) -> None:
        self.batch_size = BATCH_SIZE
        self.msk = msk
        # todo: run msk on mock data for init
        self.model = keras.models.load_model(MODEL_PATH)

    def run_segmentation(self, directory_path):
        try:
            return self._run_segmentation(directory_path)
        except Exception as e:
            message = f'Shit got fucked up! Reason: {str(e)}.'
            print('------------------------')
            print(message)
            print('------------------------')

    def _run_segmentation(self, directory_path):
        series_IDs = sitk.ImageSeriesReader.GetGDCMSeriesIDs(directory_path)
        series_file_names = sitk.ImageSeriesReader.GetGDCMSeriesFileNames(
            directory_path, series_IDs[0])
        series_reader = sitk.ImageSeriesReader()
        series_reader.SetFileNames(series_file_names)
        series_reader.LoadPrivateTagsOn()
        image3D = series_reader.Execute()
        lobe_segmentation = self.run_mask(image3D)
        infec_segmentation = self.run_models(image3D)
        feature = []
        for i_lobe in range(1, 6):
            lobe_point = infec_segmentation.copy()
            lobe_point = lobe_point[lobe_segmentation == i_lobe]
            lobe_point = lobe_point.flatten()
            feature.append(((lobe_point > 0.5).sum()) / len(lobe_point))
        feature = np.round(np.array(feature) * 100, 1)
        return str(feature)

    def run_mask(self, image3D):
        return self.msk.apply_fused(image3D,
                                    basemodel='LTRCLobes',
                                    fillmodel='R231',
                                    force_cpu=False,
                                    batch_size=8,
                                    volume_postprocessing=True,
                                    noHU=False)

    def run_models(self, image3D):
        aggregate = self.run_model_0(image3D) + self.run_model_1(image3D)
        return aggregate

    def run_model_0(self, image3D):
        self.model.load_weights(WEIGHTS_0_PATH)
        infec_segmentation = (self.model.predict(
            image3D[:, :, ::-1, :], batch_size=self.batch_size, workers=16
        )[:, :, ::-1, 0] + self.model.predict(
            image3D, batch_size=self.batch_size, workers=16)[:, :, :, 0]) / 2
        return infec_segmentation

    def run_model_1(self, image3D):
        self.model.load_weights(WEIGHTS_1_PATH)
        infec_segmentation = (self.model.predict(
            image3D[:, :, ::-1, :], batch_size=self.batch_size, workers=16
        )[:, :, ::-1, 0] + self.model.predict(
            image3D, batch_size=self.batch_size, workers=16)[:, :, :, 0]) / 2
        return infec_segmentation

    def preprocess(self, image3D):
        sss = 0.7
        ct = sitk.GetArrayViewFromImage(image3D).copy()
        ct[ct < -1024] = -1024
        sig = min((ct.shape[2] / 150.) * sss, 1)
        ct = gf(ct, sig)
        ct = self.window(ct)
        ct = np.array([ct, ct, ct]).transpose(1, 2, 3, 0)
        return ct

    @staticmethod
    def window(img, WL=-600, WW=1500):
        upper, lower = WL + WW // 2, WL - WW // 2
        X = np.clip(img.copy(), lower, upper)
        X = X - np.min(X)
        X = X / (np.max(X) / 255.0)
        return X

    @staticmethod
    def plot_slice(ct, lobe_segmentation, infec_segmentation, feature, s):
        nii_data = ct[:, :, :, 0].astype('uint8')
        nii_mask = infec_segmentation > 0.5

        contour = measure.find_contours(nii_mask[s, :, :], 0.5)

        rgb_img = cv2.merge(
            [nii_data[s, :, :], nii_data[s, :, :], nii_data[s, :, :]])

        font = cv2.FONT_HERSHEY_SIMPLEX

        main0 = rgb_img.copy()

        for t in range(len(contour)):
            i = np.array(np.round(contour[t], 0), int)
            img_pl = np.zeros((512, 512))
            cv2.fillPoly(img_pl, pts=[i[:, [1, 0]]], color=(1))
            img_pl = np.array(img_pl)
            img_pl[img_pl > 0] = 1

            img_pl = binary_dilation(img_pl,
                                     structure=np.ones((3, 3)),
                                     iterations=1)

            contour_2 = measure.find_contours(img_pl, 0.5)
            i2 = np.array(np.round(contour_2[0], 0), int)
            cv2.drawContours(rgb_img, [i2[:, [1, 0]]], -1, (255, 0, 0), 1)

        main = rgb_img.copy()

        if nii_mask[s, :, :].sum() > 0:
            cv2.putText(main0, 'YES', (5, 50), font, 2, (0, 255, 0), 2,
                        cv2.LINE_AA)
        else:
            cv2.putText(main0, 'No', (5, 50), font, 2, (255, 0, 0), 2,
                        cv2.LINE_AA)

        cv2.putText(main0, str(s), (450, 30), font, 1, (0, 0, 255), 2,
                    cv2.LINE_AA)

        RGBforLabel = {
            1: (0, 0, 204),
            2: (255, 77, 255),
            3: (255, 255, 25),
            4: (0, 255, 255),
            5: (255, 102, 25)
        }

        lobe_name = [
            'Left  Upper', 'Left  Lower', 'Right Upper', 'Right Middle',
            'Right Lower'
        ]

        for i_lobe in range(1, 6):
            seg = (lobe_segmentation[s] == i_lobe).astype('uint8')
            contours, _ = cv2.findContours(seg, cv2.RETR_EXTERNAL,
                                           cv2.CHAIN_APPROX_NONE)
            for i, c in enumerate(contours):
                mask = np.zeros(seg.shape, np.uint8)
                cv2.drawContours(mask, [c], -1, 255, -1)
                label = i_lobe
                colour = RGBforLabel.get(label)
                cv2.drawContours(main, [c], -1, colour, 1)

            colour = RGBforLabel.get(i_lobe)

            cv2.putText(main,
                        lobe_name[i_lobe - 1] + f' = {feature[i_lobe-1]}%',
                        (5, -5 + i_lobe * 20), font, 0.5, colour, 1,
                        cv2.LINE_AA)

        cv2.putText(main, 'Infection', (370, 25), font, 1, (255, 0, 0), 1,
                    cv2.LINE_AA)

        final_plot = np.concatenate((main0, main), axis=1)

        return final_plot
