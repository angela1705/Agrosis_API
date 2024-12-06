# Generated by Django 5.1 on 2024-12-06 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('bodega', '0003_initial'),
        ('bodega_insumo', '0002_delete_bodegainsumo'),
        ('insumos', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BodegaInsumo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('bodega', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bodega.bodega')),
                ('insumo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='insumos.insumo')),
            ],
        ),
    ]