from rest_framework import viewsets
from apps.Cultivo.productos_control.models import ProductoControl
from apps.Cultivo.productos_control.api.serializers import ProductoControlSerializer

class ProductoControlViewSet(viewsets.ModelViewSet):
    queryset = ProductoControl.objects.all()
    serializer_class = ProductoControlSerializer
