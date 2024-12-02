from rest_framework import viewsets
from apps.Cultivo.lotes.models import Lote
from apps.Cultivo.lotes.api.serializers import LoteSerializer

class LoteViewSet(viewsets.ModelViewSet):
    queryset = Lote.objects.all()
    serializer_class = LoteSerializer
