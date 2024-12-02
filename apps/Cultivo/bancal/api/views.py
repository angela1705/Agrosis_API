from rest_framework import viewsets
from apps.Cultivo.bancal.models import Bancal
from apps.Cultivo.bancal.api.serializers import BancalSerializer

class BancalViewSet(viewsets.ModelViewSet):
    queryset = Bancal.objects.all()
    serializer_class = BancalSerializer
