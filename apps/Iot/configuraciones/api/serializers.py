from ..models import Configuraciones
from rest_framework.serializers import ModelSerializer
class ConfiguracionesSerializer(ModelSerializer):
    class Meta:
        model = Configuraciones
        fields = '__all__'