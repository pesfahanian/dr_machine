import os

from django.db.models.signals import post_save
from django.dispatch import receiver

from inferences.core.model import COVIDSegmentationModel
from inferences.models import ChestXRayInference, COVIDCTInference
# from inferences.tasks import execute_run_segmentation, get_results
from inferences.utils.dicom_utils import read_metadata
from inferences.utils.misc import process_zipfile_case


@receiver(post_save, sender=ChestXRayInference)
def run_chest_xray_inference(sender, instance, created, **kwargs):
    if created:
        print('Running chest X-Ray inference....')
        pass


@receiver(post_save, sender=COVIDCTInference)
def run_covid_inference(sender, instance, created, **kwargs):
    if created:
        print('Running COVID-19 segmentation....')
        # metadata = read_metadata(instance.file)
        # instance.patient_id = metadata['PatientID']
        # instance.patient_sex = metadata['PatientSex']
        # instance.patient_age = int(metadata['PatientAge'][:-1])
        # instance.save()

        # model = Model()
        # report = model.run_inference(file_path=instance.file.path)

        # report = execute_run_inference.delay(file_path=instance.file.path)

        extract_path = f'{instance.cases_directory_path}/{instance.id}/'

        process_zipfile_case(instance.file.path, extract_path)

        print(extract_path)

        result_path = f'{instance.results_directory_path}/{instance.id}/'

        print(result_path)

        if not os.path.isdir(result_path):
            os.makedirs(result_path)

        model = COVIDSegmentationModel()

        model.run(directory_path=extract_path, result_path=result_path)

        # task = execute_run_segmentation.delay(directory_path=extract_path)
        # task_id = task.id
        # report = get_results(task_id)

        # model = Model()
        # report = model.run_segmentation(directory_path=extract_path)

        # print('-------', report)

        # report_save_path = f'{instance.results_directory_path}/{instance.id}.txt'
        # f = open(report_save_path, 'w')
        # f.write(str(report))
        # f.close()

        # instance.report = report
        # instance.save()
