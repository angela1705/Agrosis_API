from rest_framework import viewsets
from apps.Cultivo.tipos_residuos.models import TipoResiduo
from apps.Cultivo.tipos_residuos.api.serializers import TipoResiduoSerializer

class TipoResiduoViewSet(viewsets.ModelViewSet):
    queryset = TipoResiduo.objects.all()
    serializer_class = TipoResiduoSerializer
