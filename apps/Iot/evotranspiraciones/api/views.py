from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import Evapotranspiraciones
from .serializers import EvapotranspiracionesSerializer

class EvapotranspiracionesViewset(ModelViewSet):
    queryset = Evapotranspiraciones.objects.all()
    serializer_class = EvapotranspiracionesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]