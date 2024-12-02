from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.tipos_residuos.api.views import TipoResiduoViewSet

router = DefaultRouter()
router.register(r'tipo_residuos', TipoResiduoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
