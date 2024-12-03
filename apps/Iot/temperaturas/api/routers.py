from .views import TemperaturasViewset
from rest_framework.routers import DefaultRouter
TemperaturasRouter = DefaultRouter()

TemperaturasRouter.register(prefix='temperaturas',viewset=TemperaturasViewset,basename='temperaturas')