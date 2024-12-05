from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BodegaHerramientaViewSet

router = DefaultRouter()
router.register(r'bodega_herramienta', BodegaHerramientaViewSet, basename='bodega_herramienta')

urlpatterns = [
    path('', include(router.urls)),
]
