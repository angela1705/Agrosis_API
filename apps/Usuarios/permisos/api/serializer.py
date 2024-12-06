from rest_framework import serializers
from apps.Usuarios.permisos.models import Permiso

class PermisoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permiso
        fields = '__all__'
