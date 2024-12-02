from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.actividades.api.views import ActividadViewSet
router = DefaultRouter()
router.register(r'actividades', ActividadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
