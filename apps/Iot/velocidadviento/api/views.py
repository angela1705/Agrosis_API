from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import VelocidadViento
from .serializers import VelocidadVientoSerializer
from apps.Usuarios.usuarios.api.permissions import IsAdminOrRead

class VelocidadVientoViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminOrRead ]
    queryset = VelocidadViento.objects.all()
    serializer_class = VelocidadVientoSerializer
    