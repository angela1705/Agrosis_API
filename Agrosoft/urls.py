from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.Iot.configuraciones.api.routers import ConfiguracionesRouter
from apps.Iot.datos_meteorologicos.api.routers import Datos_metereologicosRouter
from apps.Iot.evotranspiraciones.api.routers import EvapotranspiracionesRouter
from apps.Iot.humedadambiental.api.routers import HumedadAmbientalRouter
from apps.Iot.humedadterreno.api.routers import HumedadTerrenoRouter
from apps.Iot.iluminaciones.api.routers import IluminacionesRouter
from apps.Iot.sensores.api.routers import SensoresRouter
from apps.Iot.temperaturas.api.routers import TemperaturasRouter
from apps.Iot.velocidadviento.api.routers import VelocidadVientoRouter

routerIOT = DefaultRouter()

routerIOT.registry.extend(ConfiguracionesRouter.registry)
routerIOT.registry.extend(Datos_metereologicosRouter.registry)
routerIOT.registry.extend(EvapotranspiracionesRouter.registry)
routerIOT.registry.extend(HumedadAmbientalRouter.registry)
routerIOT.registry.extend(HumedadTerrenoRouter.registry)
routerIOT.registry.extend(IluminacionesRouter.registry)
routerIOT.registry.extend(SensoresRouter.registry)
routerIOT.registry.extend(TemperaturasRouter.registry)
routerIOT.registry.extend(VelocidadVientoRouter.registry)


from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="documentacion API",
      default_version='v0.1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/iot/', include (routerIOT.urls)),
]