# Generated by Django 5.1 on 2024-12-02 02:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('lotes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bancal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=15)),
                ('TamX', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('TamY', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('posY', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('posX', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('lote', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lotes.lote')),
            ],
        ),
    ]