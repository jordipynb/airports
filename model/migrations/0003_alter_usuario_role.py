# Generated by Django 4.0.5 on 2022-06-25 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0002_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='role',
            field=models.CharField(choices=[('US', 'Usuario Comun'), ('CL', 'Cliente'), ('AD', 'Administrador Instalaciones'), ('AA', 'Administrador Aeropuertos'), ('AR', 'Administrador Reparaciones'), ('AG', 'Administrador General')], default='US', max_length=2),
        ),
    ]
