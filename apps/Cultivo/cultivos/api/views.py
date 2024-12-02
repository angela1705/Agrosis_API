from rest_framework import viewsets
from apps.Cultivo.cultivos.models import Cultivo
from apps.Cultivo.cultivos.api.serializers import CultivoSerializer

class CultivoViewSet(viewsets.ModelViewSet):
    queryset = Cultivo.objects.all()
    serializer_class = CultivoSerializer
