# Generated by Django 5.1 on 2024-12-02 02:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('actividades', '0001_initial'),
        ('cultivos', '0001_initial'),
        ('tipo_actividad', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='cultivo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultivos.cultivo'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='tipo_actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo_actividad.tipoactividad'),
        ),
        migrations.AddField(
            model_name='actividad',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]