# Generated by Django 5.1 on 2024-12-04 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('actividades', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='actividad',
            name='cantidadUsada',
            field=models.IntegerField(default=0),
        ),
    ]