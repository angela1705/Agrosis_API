from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.tipo_actividad.api.views import TipoActividadViewSet

router = DefaultRouter()
router.register(r'tipo_actividad', TipoActividadViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
