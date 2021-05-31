from django.contrib import admin

from inferences.models import ChestXRayInference, COVIDCTInference

admin.site.register(ChestXRayInference)
admin.site.register(COVIDCTInference)
