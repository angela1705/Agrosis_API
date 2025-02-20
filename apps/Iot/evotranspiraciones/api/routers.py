from .views import EvapotranspiracionesViewset
from rest_framework.routers import DefaultRouter
EvapotranspiracionesRouter = DefaultRouter()

EvapotranspiracionesRouter.register(prefix='evapotranspiraciones',viewset=EvapotranspiracionesViewset,basename='evapotranspiraciones')