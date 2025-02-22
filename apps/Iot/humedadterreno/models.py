from django.db import models
from apps.Cultivo.bancal.models import Bancal

class HumedadTerreno(models.Model):
    fk_bancal = models.ForeignKey(Bancal,on_delete=models.SET_NULL,null=True)
    porcentaje = models.IntegerField()
    fecha = models.DateTimeField()
    def __str__(self):
        return "Bancal: "+str(self.fk_bancal)+" Fecha: "+str(self.fecha)