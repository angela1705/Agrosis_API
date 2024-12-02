from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.tipo_especies.api.views import TipoEspecieViewSet

router = DefaultRouter()
router.register(r'tipo_especies', TipoEspecieViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
