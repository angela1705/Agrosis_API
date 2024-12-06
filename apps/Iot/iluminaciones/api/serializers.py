from ..models import Iluminaciones
from rest_framework.serializers import ModelSerializer

class IluminacionesSerializer(ModelSerializer):
    class Meta:
        model = Iluminaciones
        fields = '__all__'