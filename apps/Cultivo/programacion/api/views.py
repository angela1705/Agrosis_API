from rest_framework import viewsets
from apps.Cultivo.programacion.models import Programacion
from apps.Cultivo.programacion.api.serializers import ProgramacionSerializer

class ProgramacionViewSet(viewsets.ModelViewSet):
    queryset = Programacion.objects.all()
    serializer_class = ProgramacionSerializer
