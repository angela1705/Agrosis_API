from ..models import HumedadTerreno
from rest_framework.serializers import ModelSerializer

class HumedadTerrenoSerializer(ModelSerializer):
    class Meta:
        model = HumedadTerreno
        fields = '__all__'