from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.programacion.api.views import ProgramacionViewSet

router = DefaultRouter()
router.register(r'´programaciones', ProgramacionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
