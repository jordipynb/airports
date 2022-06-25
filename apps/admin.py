from django.contrib import admin

from apps.models.Aeropuerto import Aeropuerto
from apps.models.Cliente import Cliente
from apps.models.Plazas import Plazas
from apps.models.Nave import Nave
from apps.models.Vuelo import Vuelo
from apps.models.Arribo import Arribo
from apps.models.Instalacion import Instalacion
from apps.models.Servicio import Servicio
from apps.models.Valoracion import Valoracion
from apps.models.Reparacion import Reparacion
from apps.models.ReparaNave import ReparaNave
from apps.models.ReparacionesDependientes import ReparacionesDependientes

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