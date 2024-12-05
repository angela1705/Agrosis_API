from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Temperaturas
from .serializers import TemperaturasSerializer

class TemperaturasViewset(ModelViewSet):
    queryset = Temperaturas.objects.all()
    serializer_class = TemperaturasSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]