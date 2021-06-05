from django.contrib import admin

from inferences.models import ChestXRayInference, COVIDCTInference


class COVIDCTInferenceAdmin(admin.ModelAdmin):
    model = COVIDCTInference
    list_display = ('id', 'prescriber', 'timestamp', 'diagnosis', 'report',
                    'is_deleted')
    list_filter = ('id', 'prescriber', 'timestamp', 'diagnosis', 'report',
                    'is_deleted')


admin.site.register(ChestXRayInference)
admin.site.register(COVIDCTInference, COVIDCTInferenceAdmin)
