from django.db.models.signals import post_save
from django.dispatch import receiver

from inferences.core.model import Model
from inferences.models import ChestXRayInference, COVIDCTInference
from inferences.tasks import execute_run_inference
from inferences.utils.dicom_utils import read_metadata


@receiver(post_save, sender=ChestXRayInference)
def run_chest_xray_inference(sender, instance, created, **kwargs):
    if created:
        print('Running chest X-Ray inference....')
        pass


@receiver(post_save, sender=COVIDCTInference)
def run_covid_inference(sender, instance, created, **kwargs):
    if created:
        print('Running COVID-19 inference....')
        # metadata = read_metadata(instance.file)
        # instance.patient_id = metadata['PatientID']
        # instance.patient_sex = metadata['PatientSex']
        # instance.patient_age = int(metadata['PatientAge'][:-1])
        # instance.save()

        # model = Model()
        # report = model.run_inference(file_path=instance.file.path)

        report = execute_run_inference(file_path=instance.file.path)

        instance.report = report
        instance.save()
