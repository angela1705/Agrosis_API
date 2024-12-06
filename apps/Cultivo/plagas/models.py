from django.db import models

class Plaga(models.Model):
    fk_tipo_plaga = models.ForeignKey('tipo_plaga.TipoPlaga', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)
    descripcion = models.TextField()
    img = models.ImageField(upload_to='plagas_images/')

    def __str__(self):
        return self.nombre
