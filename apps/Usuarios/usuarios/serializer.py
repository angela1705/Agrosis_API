from rest_framework.serializers import ModelSerializer
from apps.Usuarios.usuarios.models import Rol, Usuarios

class RolSerializer(ModelSerializer):
    class Meta:
        model = Rol
        fields = '__all__'

class UsuarioSerializer(ModelSerializer):
    class Meta:
        model = Usuarios
        fields = '__all__'