from django.db import models
from apps.Cultivo.lotes.models import Lotes
# Create your models here.
class Datos_metereologicos(models.Model):
    fk_lote = models.ForeignKey(Lotes,on_delete=models.SET_NULL,null=True)
    nombre = models.CharField(max_length=20)
    fecha_hora = models.DateTimeField()
    tipo_dato = models.IntegerField()
    valor = models.IntegerField()
    def __str__(self):
        return self.nombre