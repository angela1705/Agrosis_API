from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from ..models import Iluminaciones
from .serializers import IluminacionesSerializer
from apps.Usuarios.usuarios.api.permissions import IsAdminOrRead

class IluminacionesViewset(ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated,IsAdminOrRead ]
    queryset = Iluminaciones.objects.all()
    serializer_class = IluminacionesSerializer
    