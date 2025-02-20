from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import HumedadAmbiental
from .serializers import HumedadAmbientalSerializer
from apps.Usuarios.usuarios.api.permissions import IsAdminOrRead

class HumedadAmbientalViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminOrRead ]
    queryset = HumedadAmbiental.objects.all()
    serializer_class = HumedadAmbientalSerializer
