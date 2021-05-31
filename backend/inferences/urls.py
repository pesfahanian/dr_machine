from rest_framework import routers

from inferences import views

default_router = routers.DefaultRouter()

default_router.register('chestxray', views.ChestXRayInferenceView)
default_router.register('covidct', views.COVIDCTInferenceView)

urlpatterns = default_router.urls
