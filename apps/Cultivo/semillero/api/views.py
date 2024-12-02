from rest_framework import viewsets
from apps.Cultivo.semillero.models import Semillero
from apps.Cultivo.semillero.api.serializers import SemilleroSerializer

class SemilleroViewSet(viewsets.ModelViewSet):
    queryset = Semillero.objects.all()
    serializer_class = SemilleroSerializer
