from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.Iot.datos_meteorologicos.api.routers import Datos_metereologicosRouter
from apps.Iot.sensores.api.routers import SensoresRouter


routerIOT = DefaultRouter()

routerIOT.registry.extend(Datos_metereologicosRouter.registry)
routerIOT.registry.extend(SensoresRouter.registry)



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