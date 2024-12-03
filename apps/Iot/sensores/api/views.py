from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Sensores
from .serializers import SensoresSerializer

class SensoresViewset(ModelViewSet):
    queryset = Sensores.objects.all()
    serializer_class = SensoresSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]