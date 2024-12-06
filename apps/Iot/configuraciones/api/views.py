from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Configuraciones
from .serializers import ConfiguracionesSerializer
from apps.Usuarios.usuarios.api.permissions import IsAdminOrRead

class ConfiguracionesViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminOrRead ]
    queryset = Configuraciones.objects.all()
    serializer_class = ConfiguracionesSerializer
    