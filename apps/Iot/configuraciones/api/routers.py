from .views import ConfiguracionesViewset
from rest_framework.routers import DefaultRouter
ConfiguracionesRouter = DefaultRouter()

ConfiguracionesRouter.register(prefix='configuraciones',viewset=ConfiguracionesViewset,basename='configuraciones')