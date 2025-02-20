from rest_framework.routers import DefaultRouter
from .views import HumedadAmbientalViewset
HumedadAmbientalRouter = DefaultRouter()
HumedadAmbientalRouter.register(prefix='humedadambiental',viewset=HumedadAmbientalViewset,basename='humedadambiental')