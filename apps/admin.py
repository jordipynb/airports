from django.contrib import admin
from .models import *

admin.site.register(Aeropuerto)
admin.site.register(Cliente)
admin.site.register(Plazas)
admin.site.register(Nave)
admin.site.register(Vuelo)
admin.site.register(Arribo)
admin.site.register(Instalacion)
admin.site.register(Servicio)
admin.site.register(Valoracion)
admin.site.register(Reparacion)
admin.site.register(ReparaNave)
admin.site.register(ReparacionesDependientes)