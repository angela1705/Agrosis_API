from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.semillero.api.views import SemilleroViewSet

router = DefaultRouter()
router.register(r'semillero', SemilleroViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
