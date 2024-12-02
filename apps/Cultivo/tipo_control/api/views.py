from rest_framework import viewsets
from apps.Cultivo.tipo_control.models import TipoControl
from apps.Cultivo.tipo_control.api.serializers import TipoControlSerializer

class TipoControlViewSet(viewsets.ModelViewSet):
    queryset = TipoControl.objects.all()
    serializer_class = TipoControlSerializer
