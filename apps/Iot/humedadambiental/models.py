from django.db import models
from apps.Iot.sensores.models import SensorAbs

class HumedadAmbiental(SensorAbs):
    porcentaje = models.IntegerField()