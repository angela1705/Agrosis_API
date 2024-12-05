from .views import IluminacionesViewset
from rest_framework.routers import DefaultRouter
IluminacionesRouter = DefaultRouter()
IluminacionesRouter.register(prefix='iluminaciones',viewset=IluminacionesViewset,basename='iluminaciones')