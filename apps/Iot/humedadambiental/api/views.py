from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import HumedadAmbiental
from .serializers import HumedadAmbientalSerializer

class HumedadAmbientalViewset(ModelViewSet):
    queryset = HumedadAmbiental.objects.all()
    serializer_class = HumedadAmbientalSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]