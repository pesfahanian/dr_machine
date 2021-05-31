import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from accounts.models import CustomUser


class BaseInference(models.Model):
    prescriber = models.ForeignKey(CustomUser,
                                   on_delete=models.SET_NULL,
                                   null=True)
    HIS_case_id = models.CharField(max_length=64, blank=True, null=True)
    HIS_patient_id = models.CharField(max_length=64, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class ChestXRayInference(BaseInference):
    class ChestXRayAbnormalities(models.TextChoices):
        NORMAL = 'NRML', _('Normal')
        ATELECTASIS = 'ATEL', _('Atelectasis')
        CARDIOMEGALY = 'CARD', _('Cardiomegaly')
        EFFUSION = 'EFFU', _('Effusion')
        INFILTRATION = 'INFL', _('Infiltration')
        MASS = 'MASS', _('Mass')
        NODULE = 'NODL', _('Nodule')
        PNEUMONIA = 'PNMN', _('Pneumonia')
        PNEUMOTHORAX = 'PNTH', _('Pneumothorax')
        CONSOLIDATION = 'CONS', _('Consolidation')
        EDEMA = 'EDMA', _('Edema')
        EMPHYSEMA = 'EMPH', _('Emphysema')
        FIBROSIS = 'FIBR', _('Fibrosis')
        PLEURALTHICKENING = 'PLTK', _('PleuralThickening')
        HERNIA = 'HERN', _('Hernia')
        OTHER = 'OTHR', _('Other')
        UNKNOWN = 'UNKN', _('Unknown')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diagnosis = models.CharField(max_length=4,
                                 choices=ChestXRayAbnormalities.choices,
                                 default=ChestXRayAbnormalities.UNKNOWN)
    report = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return str(self.id)


class COVIDCTInference(BaseInference):
    class COVIDCTAbnormalities(models.TextChoices):
        NORMAL = 'NRML', _('Normal')
        COVID19 = 'CVID', _('Covid19')
        ABNORMAL = 'ABNR', _('Abnormal')
        OTHER = 'OTHR', _('Other')
        UNKNOWN = 'UNKN', _('Unknown')

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    diagnosis = models.CharField(max_length=4,
                                 choices=COVIDCTAbnormalities.choices,
                                 default=COVIDCTAbnormalities.UNKNOWN)
    report = models.CharField(max_length=1024, blank=True, null=True)

    def __str__(self):
        return str(self.id)
