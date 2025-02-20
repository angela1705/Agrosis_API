from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from channels.layers import get_channel_layer
import asyncio
import json

#from apps.Cultivo.lotes.models import Lotes
from apps.Iot.datos_meteorologicos.models import Datos_metereologicos

# Create your models here.
class Sensores(models.Model):
    fk_datos_metereologicos = models.ForeignKey(Datos_metereologicos,on_delete=models.SET_NULL,null=True)
    tipo_sensores = models.CharField(max_length=200)
    def __str__(self) -> str:
        return "Sensor de tipo: " + str(self.tipo_sensores)
    
class SensorAbs(models.Model):
    fk_lote = models.IntegerField(null=True)
    fecha = models.DateTimeField()
    def __str__(self):
        return "Lote: "+str(self.fk_lote)+" Fecha: "+str(self.fecha)
    
@receiver(post_save, sender=Sensores)
def enviar_datos_sensores(sender, instance, **kwargs):
    channel_layer = get_channel_layer()
    
    # Formato de datos a enviar
    data = {
        "id": instance.id,
        "tipo_sensores": instance.tipo_sensores,
        "fk_datos_metereologicos_id": instance.fk_datos_metereologicos_id if instance.fk_datos_metereologicos_id else None,
    }

    async def send_data():
        await channel_layer.group_send(
            "sensores",
            {
                "type": "sensor_data",
                "message": json.dumps(data)
            }
        )
    
    # Ejecutar la tarea asíncrona
    asyncio.run(send_data())