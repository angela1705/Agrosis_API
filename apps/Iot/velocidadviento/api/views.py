from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..models import VelocidadViento
from .serializers import VelocidadVientoSerializer

class VelocidadVientoViewset(ModelViewSet):
    queryset = VelocidadViento.objects.all()
    serializer_class = VelocidadVientoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]