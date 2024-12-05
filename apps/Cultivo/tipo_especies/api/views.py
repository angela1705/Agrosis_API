from rest_framework import viewsets
from apps.Cultivo.tipo_especies.models import TipoEspecie
from apps.Cultivo.tipo_especies.api.serializers import TipoEspecieSerializer

class TipoEspecieViewSet(viewsets.ModelViewSet):
    queryset = TipoEspecie.objects.all()
    serializer_class = TipoEspecieSerializer
