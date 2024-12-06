from ..models import Temperaturas
from rest_framework.serializers import ModelSerializer

class TemperaturasSerializer(ModelSerializer):
    class Meta:
        model = Temperaturas
        fields = '__all__'