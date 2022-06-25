from django.contrib import admin

from model.models.Aeropuerto import Aeropuerto
from model.models.Cliente import Cliente
from model.models.Plazas import Plazas
from model.models.Nave import Nave
from model.models.Vuelo import Vuelo
from model.models.Arribo import Arribo
from model.models.Instalacion import Instalacion
from model.models.Servicio import Servicio
from model.models.Valoracion import Valoracion
from model.models.Reparacion import Reparacion
from model.models.ReparaNave import ReparaNave
from model.models.ReparacionesDependientes import ReparacionesDependientes

from model.models.Usuario import Usuario

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

admin.site.register(Usuario)