from .views import VelocidadVientoViewset
from rest_framework.routers import DefaultRouter
VelocidadVientoRouter = DefaultRouter()

VelocidadVientoRouter.register(prefix='velocidadviento',viewset=VelocidadVientoViewset,basename='velocidadviento')