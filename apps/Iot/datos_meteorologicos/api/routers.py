from .views import Datos_metereologicosViewset
from rest_framework.routers import DefaultRouter
Datos_metereologicosRouter = DefaultRouter()

Datos_metereologicosRouter.register(prefix='datosmetereologicos',viewset=Datos_metereologicosViewset,basename='datosmetereologicos')