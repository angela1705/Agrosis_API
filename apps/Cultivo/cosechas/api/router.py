from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.cosechas.api.views import CosechaViewSet

router = DefaultRouter()
router.register(r'cosechas', CosechaViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
