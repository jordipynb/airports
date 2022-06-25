from django.db import models

class Usuario(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    password = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    ROLE = (
        ('US', 'Usuario Comun'),
        ('CL', 'Cliente'),
        ('AD', 'Administrador Instalaciones'),
        ('AA', 'Administrador Aeropuertos'),
        ('AR', 'Administrador Reparaciones'),
        ('AG', 'Administrador General')
    )
    role = models.CharField(max_length=2, choices=ROLE, default='US', null=False)
