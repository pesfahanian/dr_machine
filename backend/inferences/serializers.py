from rest_framework import serializers

from accounts.serializers import CustomUserSerializers

from inferences.models import ChestXRayInference, COVIDCTInference


class ChestXRayInferenceSerializers(serializers.ModelSerializer):
    prescriber = CustomUserSerializers()

    class Meta:
        model = ChestXRayInference
        fields = ('id', 'prescriber', 'HIS_case_id', 'HIS_patient_id',
                  'timestamp', 'is_deleted', 'diagnosis', 'report')


class COVIDCTInferenceSerializers(serializers.ModelSerializer):
    prescriber = CustomUserSerializers()

    class Meta:
        model = COVIDCTInference
        fields = ('id', 'prescriber', 'HIS_case_id', 'HIS_patient_id',
                  'timestamp', 'is_deleted', 'diagnosis', 'report')
