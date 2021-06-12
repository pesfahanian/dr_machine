import os
import numpy as np

from tensorflow import keras
from tensorflow.keras.applications.densenet import DenseNet121
from tensorflow.keras.applications.densenet import (preprocess_input,
                                                    decode_predictions)
from tensorflow.keras.preprocessing import image

MODEL_PATH = f'{os.getcwd()}/inferences/core/imagenet.h5'


class Model:
    def __init__(self) -> None:
        self.model = keras.models.load_model(MODEL_PATH)

    def run_inference(self, file_path: str) -> str:
        prepared_file = self.prepare(file_path=file_path)
        preds = self.model.predict(prepared_file)
        return str(decode_predictions(preds, top=1)[0][0])

    @staticmethod
    def prepare(file_path: str):
        img = image.load_img(file_path, target_size=(224, 224))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)
        return x
