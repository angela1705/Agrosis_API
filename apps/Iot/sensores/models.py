from django.db import models
from apps.Cultivo.lotes.models import Lote
from apps.Iot.datos_meteorologicos.models import Datos_metereologicos

# Create your models here.
class Sensores(models.Model):
    fk_datos_metereologicos = models.ForeignKey(Datos_metereologicos,on_delete=models.SET_NULL,null=True)
    tipo_sensores = models.CharField(max_length=200)
    def __str__(self) -> str:
        return "Sensor de tipo: " + str(self.tipo_sensores)
    
class SensorAbs(models.Model):
    fk_lote = models.ForeignKey(Lote,on_delete=models.SET_NULL,null=True)
    fecha = models.DateTimeField()
    def __str__(self):
        return "Lote: "+str(self.fk_lote)+" Fecha: "+str(self.fecha)