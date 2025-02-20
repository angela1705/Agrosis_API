from django.db import models
from apps.Iot.sensores.models import SensorAbs

class Temperaturas(SensorAbs):
    lumens = models.IntegerField()