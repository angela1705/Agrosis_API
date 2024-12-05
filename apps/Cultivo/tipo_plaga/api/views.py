from rest_framework import viewsets
from apps.Cultivo.tipo_plaga.models import TipoPlaga
from apps.Cultivo.tipo_plaga.api.serializers import TipoPlagaSerializer

class TipoPlagaViewSet(viewsets.ModelViewSet):
    queryset = TipoPlaga.objects.all()
    serializer_class = TipoPlagaSerializer
