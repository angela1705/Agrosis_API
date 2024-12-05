from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Configuraciones
from .serializers import ConfiguracionesSerializer

class ConfiguracionesViewset(ModelViewSet):
    queryset = Configuraciones.objects.all()
    serializer_class = ConfiguracionesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]