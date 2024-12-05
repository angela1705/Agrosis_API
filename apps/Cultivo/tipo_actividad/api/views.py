from rest_framework import viewsets
from apps.Cultivo.tipo_actividad.models import TipoActividad
from apps.Cultivo.tipo_actividad.api.serializers import TipoActividadSerializer

class TipoActividadViewSet(viewsets.ModelViewSet):
    queryset = TipoActividad.objects.all()
    serializer_class = TipoActividadSerializer
