from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Iluminaciones
from .serializers import IluminacionesSerializer

class IluminacionesViewset(ModelViewSet):
    queryset = Iluminaciones.objects.all()
    serializer_class = IluminacionesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]