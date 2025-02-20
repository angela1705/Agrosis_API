from django.db import models
from apps.Iot.sensores.models import SensorAbs

class Iluminaciones(SensorAbs):
    lumens = models.IntegerField()