# Generated by Django 5.1.2 on 2024-12-06 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rol_permiso', '0003_alter_rolpermiso_rol'),
        ('roles_acciones', '0003_alter_rolaccion_rol'),
        ('usuario_rol', '0003_alter_usuariorol_rol'),
        ('usuarios', '0002_roles_alter_usuarios_rol'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Rol',
        ),
    ]
