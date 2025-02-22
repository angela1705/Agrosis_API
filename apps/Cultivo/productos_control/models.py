from django.db import models

class ProductoControl(models.Model):
    precio = models.IntegerField()
    nombre = models.CharField(max_length=30)
    compuestoActivo = models.CharField(max_length=50)
    fichaTecnica = models.TextField()
    Contenido = models.IntegerField()
    tipoContenido = models.CharField(max_length=10)
    unidades = models.IntegerField()

    def __str__(self):
        return self.nombre
