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
    path('tipo_plaga/', include('apps.Cultivo.tipo_plaga.api.router')),  
    path('plagas/', include('apps.Cultivo.plagas.api.router')), 
    path('productos_control/', include('apps.Cultivo.productos_control.api.router')),  
    path('tipo_control/', include('apps.Cultivo.tipo_control.api.router')), 
    path('controles/', include('apps.Cultivo.controles.api.router')), 
    path('especies/', include('apps.Cultivo.especies.api.router')),  
    path('tipo_especies/', include('apps.Cultivo.tipo_especies.api.router')),  
    path('cultivos/', include('apps.Cultivo.cultivos.api.router')), 
    path('fase_lunar/', include('apps.Cultivo.fase_lunar.api.router')),  
    path('semillero/', include('apps.Cultivo.semillero.api.router')),  
    path('bancal/', include('apps.Cultivo.bancal.api.router')),
    path('actividades/', include('apps.Cultivo.actividades.api.router')),  
    path('tipo_actividad/', include('apps.Cultivo.tipo_actividad.api.router')),  
    path('plantaciones/', include('apps.Cultivo.plantaciones.api.router')), 
    path('afecciones/', include('apps.Cultivo.afecciones.api.router')),  
    path('residuos/', include('apps.Cultivo.residuos.api.router')),
    path('tipos_residuos/', include('apps.Cultivo.tipos_residuos.api.router')),
    path('programacion/', include('apps.Cultivo.programacion.api.router')),
    path('cosechas/', include('apps.Cultivo.cosechas.api.router')),
    path('lotes/', include('apps.Cultivo.lotes.api.router')),



    
]

