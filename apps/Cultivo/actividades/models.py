from django.db import models


class Actividad(models.Model):
    tipo_actividad = models.ForeignKey('tipo_actividad.TipoActividad', on_delete=models.CASCADE)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    usuario = models.ForeignKey('usuarios.Usuarios', on_delete=models.CASCADE)
    cultivo = models.ForeignKey('cultivos.Cultivo', on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo_actividad
