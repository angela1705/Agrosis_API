from django.urls import path, include
from rest_framework.routers import DefaultRouter
from apps.Cultivo.productos_control.api.views import ProductoControlViewSet

router = DefaultRouter()
router.register(r'productos_control', ProductoControlViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
