from rest_framework import viewsets
from apps.Cultivo.controles.models import Control
from apps.Cultivo.controles.api.serializers import ControlSerializer

class ControlViewSet(viewsets.ModelViewSet):
    queryset = Control.objects.all()
    serializer_class = ControlSerializer
