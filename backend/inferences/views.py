from rest_framework import viewsets

from inferences.models import ChestXRayInference, COVIDCTInference
from inferences.serializers import (ChestXRayInferenceSerializers,
                                    COVIDCTInferenceSerializers)


class ChestXRayInferenceView(viewsets.ModelViewSet):
    lookup_url_kwarg = 'id'
    queryset = ChestXRayInference.objects.all()

    def get_serializer_class(self):
        return ChestXRayInferenceSerializers

    def filter_queryset(self, queryset):
        queryset = self.get_queryset().filter(creator=self.request.user)
        return queryset


class COVIDCTInferenceView(viewsets.ModelViewSet):
    lookup_url_kwarg = 'id'
    queryset = COVIDCTInference.objects.all()

    def get_serializer_class(self):
        return COVIDCTInferenceSerializers

    def filter_queryset(self, queryset):
        queryset = self.get_queryset().filter(creator=self.request.user)
        return queryset
