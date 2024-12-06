from django.db import models
from apps.Iot.sensores.models import Sensores

# Create your models here.
class Configuraciones(models.Model):
    fk_sensores = models.ForeignKey(Sensores,on_delete=models.SET_NULL,null=True)
    parametros = models.IntegerField()
    def __str__(self) -> str:
        return "Configuración: "+ str(self.parametros)