from rest_framework.routers import DefaultRouter
from .views import HumedadTerrenoViewset
HumedadTerrenoRouter = DefaultRouter()
HumedadTerrenoRouter.register(prefix='humedadterreno',viewset=HumedadTerrenoViewset,basename='humedadterreno')