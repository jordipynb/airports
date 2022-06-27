from django.shortcuts import render
from django.contrib import messages

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

def listar(request):
    dict=para_listar(request)
    return render(request, "listados.html", dict)

def para_listar(request):
    data = request.POST['data']
    listado=[]
    if data == "Aeropuerto":
        listado = Aeropuerto.objects.all()
    elif data == "Cliente":
        listado = Cliente.objects.all()
    elif data == "Nave":
        listado = Nave.objects.all()
    elif data == "Vuelo":
        listado = Vuelo.objects.all()
    elif data == "Arribo":
        listado = Arribo.objects.all()
    elif data == "Instalacion":
        listado = Instalacion.objects.all()
    elif data == "Servicio":
        listado = Servicio.objects.all()
    elif data == "Valoracion":
        listado = Valoracion.objects.all()
    elif data == "Reparacion":
        listado = Reparacion.objects.all()
    elif data == "ReparaNave":
        listado = ReparaNave.objects.all()
    elif data == "ReparacionesDependientes":
        listado = ReparacionesDependientes.objects.all()
    messages.success(request, 'Listados!')
    campos=[]
    for a in listado:
        campos=a.campos()
        break
    return {"campos": campos,"aeropuertos": listado,"tabla":data}

