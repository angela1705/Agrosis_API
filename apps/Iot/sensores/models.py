from django.db import models
from apps.Iot.datos_meteorologicos.models import Datos_metereologicos

# Create your models here.
class Sensores(models.Model):
    fk_datos_metereologicos = models.ForeignKey(Datos_metereologicos,on_delete=models.SET_NULL,null=True)
    tipo_sensores = models.CharField(max_length=200)
    def __str__(self) -> str:
        return "Sensor de tipo: " + str(self.tipo_sensores)