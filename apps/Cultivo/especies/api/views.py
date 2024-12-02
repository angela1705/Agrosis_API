from rest_framework import viewsets
from apps.Cultivo.especies.models import Especie
from apps.Cultivo.especies.api.serializers import EspecieSerializer

class EspecieViewSet(viewsets.ModelViewSet):
    queryset = Especie.objects.all()
    serializer_class = EspecieSerializer
