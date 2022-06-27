from django.contrib import messages
from django.shortcuts import redirect

from model.models.Aeropuerto import Aeropuerto
from model.models.Cliente import Cliente
from model.models.Nave import Nave
from model.models.Vuelo import Vuelo
from model.models.Arribo import Arribo
from model.models.Instalacion import Instalacion
from model.models.Servicio import Servicio
from model.models.Valoracion import Valoracion
from model.models.Reparacion import Reparacion
from model.models.ReparaNave import ReparaNave
from model.models.ReparacionesDependientes import ReparacionesDependientes

def eliminar(request,codigo,tabla):
    if tabla== "Aeropuerto":
        elemento = Aeropuerto.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "Cliente":
        elemento = Cliente.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "Nave":
        elemento = Nave.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "Vuelo":
        elemento = Vuelo.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "Arribo":
        elemento= Arribo.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "Instalacion":
        elemento= Instalacion.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "Servicio":
        elemento= Servicio.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "Valoracion":
        elemento= Valoracion.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "Reparacion":
        elemento= Reparacion.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "ReparaNave":
        elemento= ReparaNave.objects.get(id=codigo)
        elemento.delete()
    elif tabla== "ReparacionesDependientes":
        elemento= ReparacionesDependientes.objects.get(id=codigo)
        elemento.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('/')

