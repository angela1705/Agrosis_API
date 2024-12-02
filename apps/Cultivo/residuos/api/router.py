from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.residuos.api.views import ResiduoViewSet

router = DefaultRouter()
router.register(r'residuos', ResiduoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
