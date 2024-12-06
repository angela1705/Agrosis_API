# Generated by Django 5.1 on 2024-12-04 04:12

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cultivos', '0002_initial'),
        ('insumos', '0001_initial'),
        ('tipo_actividad', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actividad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_inicio', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('cantidadUsada', models.IntegerField(default=0)),
                ('cultivo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cultivos.cultivo')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.insumo')),
                ('tipo_actividad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tipo_actividad.tipoactividad')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
