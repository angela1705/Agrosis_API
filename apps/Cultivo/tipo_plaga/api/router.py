from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.tipo_plaga.api.views import TipoPlagaViewSet

router = DefaultRouter()
router.register(r'tipo_plaga', TipoPlagaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
