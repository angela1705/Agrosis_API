# Generated by Django 5.1 on 2024-12-06 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('datos_meteorologicos', '0001_initial'),
        ('lotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SensorAbs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField()),
                ('fk_lote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='lotes.lote')),
            ],
        ),
        migrations.CreateModel(
            name='Sensores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_sensores', models.CharField(max_length=200)),
                ('fk_datos_metereologicos', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='datos_meteorologicos.datos_metereologicos')),
            ],
        ),
    ]