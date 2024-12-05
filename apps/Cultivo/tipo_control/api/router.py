from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.tipo_control.api.views import TipoControlViewSet

router = DefaultRouter()
router.register(r'tipo_control', TipoControlViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
