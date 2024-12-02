from rest_framework import viewsets
from apps.Cultivo.cosechas.models import Cosecha
from apps.Cultivo.cosechas.api.serializers import CosechaSerializer

class CosechaViewSet(viewsets.ModelViewSet):
    queryset = Cosecha.objects.all()
    serializer_class = CosechaSerializer
