from django.db import models
from apps.Cultivo.lotes.models import Lotes
# Create your models here.

class Evapotranspiraciones(models.Model):
    fk_lote = models.ForeignKey(Lotes,on_delete=models.SET_NULL,null=True)
    milimetrosMCuadrado = models.FloatField()
    fecha = models.DateTimeField()
    def __str__(self) -> str:
        return "Lote: "+str(self.fk_lote)+" Fecha: "+str(self.fecha)