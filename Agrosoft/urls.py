from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.Iot.configuraciones.api.routers import ConfiguracionesRouter
from apps.Iot.datos_meteorologicos.api.routers import Datos_metereologicosRouter
from apps.Iot.evotranspiraciones.api.routers import EvapotranspiracionesRouter
from apps.Iot.humedadambiental.api.routers import HumedadAmbientalRouter
from apps.Iot.humedadterreno.api.routers import HumedadAmbientalRouter
from apps.Iot.iluminaciones.api.routers import IluminacionesRouter
from apps.Iot.sensores.api.routers import SensoresRouter
from apps.Iot.temperaturas.api.routers import TemperaturasRouter
from apps.Iot.velocidadviento.api.routers import VelocidadVientoRouter
from rest_framework.routers import DefaultRouter
from apps.Inventario.bodega.api.routers import bodegaRouter
from apps.Inventario.bodega_herramienta.api.routers import bodegaHerramientaRouter
from apps.Inventario.bodega_insumo.api.routers import bodegaInsumoRouter
from apps.Inventario.herramientas.api.routers import herramientaRouter
from apps.Inventario.insumos.api.routers import insumoRouter
from apps.Cultivo.actividades.api.router import actividadRouter 
from apps.Cultivo.afecciones.api.router import afeccionRouter 
from apps.Cultivo.bancal.api.router import bancalRouter 
from apps.Cultivo.controles.api.router import controlRouter 
from apps.Cultivo.cosechas.api.router import cosechaRouter 
from apps.Cultivo.cultivos.api.router import cultivoRouter 
from apps.Cultivo.especies.api.router import especiesRouter 
from apps.Cultivo.fase_lunar.api.router import faseLunarRouter 
from apps.Cultivo.lotes.api.router import lotesRouter 
from apps.Cultivo.plagas.api.router import plagasRouter 
from apps.Cultivo.plantaciones.api.router import plantacionRouter 
from apps.Cultivo.productos_control.api.router import productosControlRouter 
from apps.Cultivo.programacion.api.router import programacionRouter 
from apps.Cultivo.residuos.api.router import residuosRouter 
from apps.Cultivo.semillero.api.router import semilleroRouter 
from apps.Cultivo.tipo_actividad.api.router import tipoActividadRouter 
from apps.Cultivo.tipo_control.api.router import tipoControlRouter 
from apps.Cultivo.tipo_especies.api.router import tipoEspecieRouter 
from apps.Cultivo.tipo_plaga.api.router import tipoPlagaRouter 
from apps.Cultivo.tipos_residuos.api.router import tipoResiduoRouter 
from apps.Cultivo.semillero_herramienta.api.router import semilleroHRouter
from apps.Cultivo.semillero_insumo.api.router import semilleroInsumoRouter
from apps.Cultivo.tareas.api.router import tareaRouter


router = DefaultRouter()

router.registry.extend(ConfiguracionesRouter.registry)
router.registry.extend(Datos_metereologicosRouter.registry)
router.registry.extend(EvapotranspiracionesRouter.registry)
router.registry.extend(HumedadAmbientalRouter.registry)
router.registry.extend(HumedadAmbientalRouter.registry)
router.registry.extend(IluminacionesRouter.registry)
router.registry.extend(SensoresRouter.registry)
router.registry.extend(TemperaturasRouter.registry)
router.registry.extend(VelocidadVientoRouter.registry)
router.registry.extend(bodegaRouter.registry)
router.registry.extend(bodegaHerramientaRouter.registry)
router.registry.extend(bodegaInsumoRouter.registry)
router.registry.extend(herramientaRouter.registry)
router.registry.extend(insumoRouter.registry)
router.registry.extend(actividadRouter.registry)
router.registry.extend(afeccionRouter.registry)
router.registry.extend(bancalRouter.registry)
router.registry.extend(controlRouter.registry)
router.registry.extend(cosechaRouter.registry)
router.registry.extend(cultivoRouter.registry)
router.registry.extend(especiesRouter.registry)
router.registry.extend(faseLunarRouter.registry)
router.registry.extend(lotesRouter.registry)
router.registry.extend(plagasRouter.registry)
router.registry.extend(plantacionRouter.registry)
router.registry.extend(productosControlRouter.registry)
router.registry.extend(programacionRouter.registry)
router.registry.extend(residuosRouter.registry)
router.registry.extend(semilleroRouter.registry)
router.registry.extend(tipoActividadRouter.registry)
router.registry.extend(tipoControlRouter.registry)
router.registry.extend(tipoEspecieRouter.registry)
router.registry.extend(tipoPlagaRouter.registry)
router.registry.extend(tipoResiduoRouter.registry)
router.registry.extend(semilleroHRouter.registry)
router.registry.extend(semilleroInsumoRouter.registry)
router.registry.extend(tareaRouter.registry)




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
    path('api/', include(router.urls)),
    path('', include('apps.Usuarios.usuarios.api.router')),
    
]

