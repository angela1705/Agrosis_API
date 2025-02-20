from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.Finanzas.salario.api.router import salarioRouter
from apps.Usuarios.permisos.api.routers import PermisosRouter
from apps.Usuarios.rol_permiso.api.routers import RolPermisoRouter
from apps.Usuarios.roles_acciones.api.routers import RolesAccionesRouter
from apps.Usuarios.usuario_rol.api.routers import UsuarioRolRouter
from apps.Usuarios.usuarios.api.routers import UsuariosRouter



router = DefaultRouter()

router.registry.extend(salarioRouter.registry)
router.registry.extend(PermisosRouter.registry)
router.registry.extend(RolPermisoRouter.registry)
router.registry.extend(UsuarioRolRouter.registry)
router.registry.extend(UsuariosRouter.registry)
router.registry.extend(RolesAccionesRouter.registry)


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

