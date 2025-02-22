from ..models import HumedadAmbiental
from rest_framework.serializers import ModelSerializer

class HumedadAmbientalSerializer(ModelSerializer):
    class Meta:
        model = HumedadAmbiental
        fields = '__all__'