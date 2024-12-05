from rest_framework import viewsets
from apps.Cultivo.plantaciones.models import Plantacion
from apps.Cultivo.plantaciones.api.serializers import PlantacionSerializer

class PlantacionViewSet(viewsets.ModelViewSet):
    queryset = Plantacion.objects.all()
    serializer_class = PlantacionSerializer
