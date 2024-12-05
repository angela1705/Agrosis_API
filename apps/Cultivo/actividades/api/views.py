from rest_framework import viewsets
from apps.Cultivo.actividades.models import Actividad
from apps.Cultivo.actividades.api.serializers import ActividadSerializer

class ActividadViewSet(viewsets.ModelViewSet):
    queryset = Actividad.objects.all()
    serializer_class = ActividadSerializer
