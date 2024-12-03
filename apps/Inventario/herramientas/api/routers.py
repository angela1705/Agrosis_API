from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HerramientaViewSet

router = DefaultRouter()
router.register(r'herramienta', HerramientaViewSet, basename='herramienta')

urlpatterns = [
    path('', include(router.urls)),
]
