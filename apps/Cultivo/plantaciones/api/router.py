from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.plantaciones.api.views import PlantacionViewSet

router = DefaultRouter()
router.register(r'plantaciones', PlantacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
