from rest_framework import viewsets
from apps.Cultivo.plagas.models import Plaga
from apps.Cultivo.plagas.api.serializers import PlagaSerializer

class PlagaViewSet(viewsets.ModelViewSet):
    queryset = Plaga.objects.all()
    serializer_class = PlagaSerializer
