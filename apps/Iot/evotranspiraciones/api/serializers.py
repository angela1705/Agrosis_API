from ..models import Evapotranspiraciones
from rest_framework.serializers import ModelSerializer
class EvapotranspiracionesSerializer(ModelSerializer):
    class Meta:
        model = Evapotranspiraciones
        fields = '__all__'