from django.db import models
from apps.Cultivo.lotes.models import Lotes

# Create your models here.
class HumedadAmbiental(models.Model):
    fk_lote = models.ForeignKey(Lotes,on_delete=models.SET_NULL,null=True)
    fecha = models.DateTimeField()
    porcentaje = models.IntegerField()
    def __str__(self):
        return "Lote: "+str(self.fk_lote)+" Fecha: "+str(self.fecha)