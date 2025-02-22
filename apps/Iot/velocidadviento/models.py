from django.db import models
from apps.Iot.sensores.models import SensorAbs

class VelocidadViento(SensorAbs):
    velocidadKmH = models.IntegerField()