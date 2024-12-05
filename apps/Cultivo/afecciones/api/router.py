from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.afecciones.api.views import AfeccionViewSet

router = DefaultRouter()
router.register(r'afecciones', AfeccionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
