from rest_framework import viewsets
from ..models import BodegaInsumo
from .serializers import BodegaInsumoSerializer

class BodegaInsumoViewSet(viewsets.ModelViewSet):
    queryset = BodegaInsumo.objects.all()
    serializer_class = BodegaInsumoSerializer
