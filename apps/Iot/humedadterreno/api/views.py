from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import HumedadTerreno
from .serializers import HumedadTerrenoSerializer

class HumedadTerrenoViewset(ModelViewSet):
    queryset = HumedadTerreno.objects.all()
    serializer_class = HumedadTerrenoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]