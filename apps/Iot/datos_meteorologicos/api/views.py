from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Datos_metereologicos
from .serializers import Datos_metereologicosSerializer

class Datos_metereologicosViewset(ModelViewSet):
    queryset = Datos_metereologicos.objects.all()
    serializer_class = Datos_metereologicosSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]