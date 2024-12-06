from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Temperaturas
from .serializers import TemperaturasSerializer
from apps.Usuarios.usuarios.api.permissions import IsAdminOrRead

class TemperaturasViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminOrRead ]
    queryset = Temperaturas.objects.all()
    serializer_class = TemperaturasSerializer
