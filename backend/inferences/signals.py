from django.db.models.signals import post_save
from django.dispatch import receiver

from inferences.models import ChestXRayInference, COVIDCTInference
from inferences.utils.dicom_utils import read_metadata


@receiver(post_save, sender=ChestXRayInference)
def run_chest_xray_diagnosis(sender, instance, created, **kwargs):
    if created:
        print('Running chest X-Ray diagnosis....')
        pass


@receiver(post_save, sender=COVIDCTInference)
def run_covid_diagnosis(sender, instance, created, **kwargs):
    if created:
        print('Running COVID-19 diagnosis....')
        metadata = read_metadata(instance.file)
        instance.patient_id = metadata['PatientID']
        instance.patient_sex = metadata['PatientSex']
        if (metadata['PatientBirthDate'] != ""):
            instance.patient_birthday = metadata['PatientBirthDate']
        instance.save()
