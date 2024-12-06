from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import HumedadTerreno
from .serializers import HumedadTerrenoSerializer
from apps.Usuarios.usuarios.api.permissions import IsAdminOrRead

class HumedadTerrenoViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminOrRead ]
    queryset = HumedadTerreno.objects.all()
    serializer_class = HumedadTerrenoSerializer
    