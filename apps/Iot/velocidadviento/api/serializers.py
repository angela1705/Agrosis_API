from ..models import VelocidadViento
from rest_framework.serializers import ModelSerializer

class VelocidadVientoSerializer(ModelSerializer):
    class Meta:
        model = VelocidadViento
        fields = '__all__'