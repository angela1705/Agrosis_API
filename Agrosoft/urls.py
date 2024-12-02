from django.contrib import admin
from django.urls import path, include


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
    path('tipo_plaga/', include('apps.Cultivo.tipo_plaga.api.router')),  # Rutas de la app tipo_plaga
    path('plagas/', include('apps.Cultivo.plagas.api.router')),  # Rutas de la app plagas
    path('productos_control/', include('apps.Cultivo.productos_control.api.router')),  # Rutas de productos control
    path('tipo_control/', include('apps.Cultivo.tipo_control.api.router')),  # Rutas de tipo_control
    path('controles/', include('apps.Cultivo.controles.api.router')),  # Rutas de controles
    
    # Apps relacionadas con especies y cultivos
    path('especies/', include('apps.Cultivo.especies.api.router')),  # Rutas de especies
    path('tipo_especies/', include('apps.Cultivo.tipo_especies.api.router')),  # Rutas de tipo_especies
    path('cultivos/', include('apps.Cultivo.cultivos.api.router')),  # Rutas de cultivos
    path('fase_lunar/', include('apps.Cultivo.fase_lunar.api.router')),  # Rutas de fase_lunar
    
    # Apps relacionadas con semillero y bodega
    path('semillero/', include('apps.Cultivo.semillero.api.router')),  # Rutas de semillero
    path('bancal/', include('apps.Cultivo.bancal.api.router')),
    
    # Apps relacionadas con tareas y actividades
    path('actividades/', include('apps.Cultivo.actividades.api.router')),  # Rutas de actividades
    path('tipo_actividad/', include('apps.Cultivo.tipo_actividad.api.router')),  # Rutas de tipo_actividad
    
    # Apps relacionadas con plantaciones, roles y usuarios
    path('plantaciones/', include('apps.Cultivo.plantaciones.api.router')),  # Rutas de plantaciones
    path('afecciones/', include('apps.Cultivo.afecciones.api.router')),  # Rutas de afecciones
    path('residuos/', include('apps.Cultivo.residuos.api.router')),
    path('tipos_residuos/', include('apps.Cultivo.tipos_residuos.api.router')),
    path('programacion/', include('apps.Cultivo.programacion.api.router')),
    path('cosechas/', include('apps.Cultivo.cosechas.api.router')),
    path('lotes/', include('apps.Cultivo.lotes.api.router')),



    
]

