# Generated by Django 5.1 on 2024-12-01 20:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductoControl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.IntegerField()),
                ('nombre', models.CharField(max_length=30)),
                ('compuestoActivo', models.CharField(max_length=50)),
                ('fichaTecnica', models.TextField()),
                ('Contenido', models.IntegerField()),
                ('tipoContenido', models.CharField(max_length=10)),
                ('unidades', models.IntegerField()),
            ],
        ),
    ]