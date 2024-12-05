from rest_framework import viewsets
from ..models import BodegaHerramienta
from .serializers import BodegaHerramientaSerializer

class BodegaHerramientaViewSet(viewsets.ModelViewSet):
    queryset = BodegaHerramienta.objects.all()
    serializer_class = BodegaHerramientaSerializer
