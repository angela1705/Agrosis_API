from rest_framework import viewsets
from apps.Cultivo.residuos.models import Residuo
from apps.Cultivo.residuos.api.serializers import ResiduoSerializer

class ResiduoViewSet(viewsets.ModelViewSet):
    queryset = Residuo.objects.all()
    serializer_class = ResiduoSerializer
