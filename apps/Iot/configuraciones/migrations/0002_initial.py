# Generated by Django 5.1 on 2024-12-06 04:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('configuraciones', '0001_initial'),
        ('sensores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuraciones',
            name='fk_sensores',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='sensores.sensores'),
        ),
    ]
