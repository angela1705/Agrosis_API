from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Evapotranspiraciones
from .serializers import EvapotranspiracionesSerializer
from apps.Usuarios.usuarios.api.permissions import IsAdminOrRead

class EvapotranspiracionesViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsAdminOrRead ]
    queryset = Evapotranspiraciones.objects.all()
    serializer_class = EvapotranspiracionesSerializer
    