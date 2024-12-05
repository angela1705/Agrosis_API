from rest_framework import viewsets
from apps.Cultivo.afecciones.models import Afeccion
from apps.Cultivo.afecciones.api.serializers import AfeccionSerializer

class AfeccionViewSet(viewsets.ModelViewSet):
    queryset = Afeccion.objects.all()
    serializer_class = AfeccionSerializer
