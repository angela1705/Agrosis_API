from rest_framework.routers import DefaultRouter
from .views import HumedadTerrenoViewset
HumedadAmbientalRouter = DefaultRouter()
HumedadAmbientalRouter.register(prefix='humedadterreno',viewset=HumedadTerrenoViewset,basename='humedadterreno')