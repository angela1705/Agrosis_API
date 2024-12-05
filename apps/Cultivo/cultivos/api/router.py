from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.cultivos.api.views import CultivoViewSet

router = DefaultRouter()
router.register(r'cultivos', CultivoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
