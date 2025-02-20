from django.db import models

class TipoResiduo(models.Model):
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.nombre
