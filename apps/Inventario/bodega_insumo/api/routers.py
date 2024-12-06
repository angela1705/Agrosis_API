from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BodegaInsumoViewSet

router = DefaultRouter()
router.register(r'bodega_insumo', BodegaInsumoViewSet, basename='bodega_insumo')

urlpatterns = [
    path('', include(router.urls)),
]
