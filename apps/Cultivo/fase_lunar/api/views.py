from rest_framework import viewsets
from apps.Cultivo.fase_lunar.models import FaseLunar
from apps.Cultivo.fase_lunar.api.serializers import FaseLunarSerializer

class FaseLunarViewSet(viewsets.ModelViewSet):
    queryset = FaseLunar.objects.all()
    serializer_class = FaseLunarSerializer
