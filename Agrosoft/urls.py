from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Router Usuarios
from apps.Usuarios.permisos.api.routers import PermisosRouter
from apps.Usuarios.rol_permiso.api.routers import RolPermisoRouter
from apps.Usuarios.roles_acciones.api.routers import RolesAccionesRouter
from apps.Usuarios.usuario_rol.api.routers import UsuarioRolRouter
from apps.Usuarios.usuarios.api.routers import UsuariosRouter
from apps.Usuarios.roles.api.routers import RolesRouter

# Router Cultivo
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

# Router Finanzas
from apps.Finanzas.pagos.api.router import pagoRouter
from apps.Finanzas.salario.api.router import salarioRouter
from apps.Finanzas.venta.api.router import ventaRouter

# Router Inventario
from apps.Inventario.bodega.api.routers import bodegaRouter
from apps.Inventario.bodega_herramienta.api.routers import bodegaHerramientaRouter
from apps.Inventario.bodega_insumo.api.routers import bodegaInsumoRouter
from apps.Inventario.herramientas.api.routers import herramientaRouter
from apps.Inventario.insumos.api.routers import insumoRouter

# Router IOT
from apps.Iot.configuraciones.api.routers import ConfiguracionesRouter
from apps.Iot.datos_meteorologicos.api.routers import Datos_metereologicosRouter
from apps.Iot.evotranspiraciones.api.routers import EvapotranspiracionesRouter
from apps.Iot.humedadambiental.api.routers import HumedadAmbientalRouter
from apps.Iot.humedadterreno.api.routers import HumedadTerrenoRouter
from apps.Iot.iluminaciones.api.routers import IluminacionesRouter
from apps.Iot.sensores.api.routers import SensoresRouter
from apps.Iot.temperaturas.api.routers import TemperaturasRouter
from apps.Iot.velocidadviento.api.routers import VelocidadVientoRouter

# Crear routers
router = DefaultRouter()
routerUsuarios = DefaultRouter()
routerCultivo = DefaultRouter()
routerFinanzas = DefaultRouter()
routerInventario = DefaultRouter()
routerIot = DefaultRouter()

# Usuarios
routerUsuarios.registry.extend(PermisosRouter.registry)
routerUsuarios.registry.extend(RolPermisoRouter.registry)
routerUsuarios.registry.extend(UsuarioRolRouter.registry)
routerUsuarios.registry.extend(UsuariosRouter.registry)
routerUsuarios.registry.extend(RolesAccionesRouter.registry)
routerUsuarios.registry.extend(RolesRouter.registry)

# Cultivo
routerCultivo.registry.extend(actividadRouter.registry)
routerCultivo.registry.extend(afeccionRouter.registry)
routerCultivo.registry.extend(bancalRouter.registry)
routerCultivo.registry.extend(controlRouter.registry)
routerCultivo.registry.extend(cosechaRouter.registry)
routerCultivo.registry.extend(cultivoRouter.registry)
routerCultivo.registry.extend(especiesRouter.registry)
routerCultivo.registry.extend(faseLunarRouter.registry)
routerCultivo.registry.extend(lotesRouter.registry)
routerCultivo.registry.extend(plagasRouter.registry)
routerCultivo.registry.extend(plantacionRouter.registry)
routerCultivo.registry.extend(productosControlRouter.registry)
routerCultivo.registry.extend(programacionRouter.registry)
routerCultivo.registry.extend(residuosRouter.registry)
routerCultivo.registry.extend(semilleroRouter.registry)
routerCultivo.registry.extend(tipoActividadRouter.registry)
routerCultivo.registry.extend(tipoControlRouter.registry)
routerCultivo.registry.extend(tipoEspecieRouter.registry)
routerCultivo.registry.extend(tipoPlagaRouter.registry)
routerCultivo.registry.extend(tipoResiduoRouter.registry)
routerCultivo.registry.extend(semilleroHRouter.registry)
routerCultivo.registry.extend(semilleroInsumoRouter.registry)
routerCultivo.registry.extend(tareaRouter.registry)

# Finanzas
routerFinanzas.registry.extend(pagoRouter.registry)
routerFinanzas.registry.extend(salarioRouter.registry)
routerFinanzas.registry.extend(ventaRouter.registry)

# Inventario
routerInventario.registry.extend(bodegaRouter.registry)
routerInventario.registry.extend(bodegaHerramientaRouter.registry)
routerInventario.registry.extend(bodegaInsumoRouter.registry)
routerInventario.registry.extend(herramientaRouter.registry)
routerInventario.registry.extend(insumoRouter.registry)

# IoT
routerIot.registry.extend(ConfiguracionesRouter.registry)
routerIot.registry.extend(Datos_metereologicosRouter.registry)
routerIot.registry.extend(EvapotranspiracionesRouter.registry)
routerIot.registry.extend(HumedadAmbientalRouter.registry)
routerIot.registry.extend(HumedadTerrenoRouter.registry)
routerIot.registry.extend(IluminacionesRouter.registry)
routerIot.registry.extend(SensoresRouter.registry)
routerIot.registry.extend(TemperaturasRouter.registry)
routerIot.registry.extend(VelocidadVientoRouter.registry)

# Documentación API
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentación API",
      default_version='v0.1',
      description="Descripción de la API",
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
    path('usuarios/', include(routerUsuarios.urls)),
    path('cultivo/', include(routerCultivo.urls)),
    path('iot/', include(routerIot.urls)),
    path('finanzas/', include(routerFinanzas.urls)),
    path('inventario/', include(routerInventario.urls)),
    path('', include('apps.Usuarios.usuarios.api.router')),
]

