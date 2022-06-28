from django.shortcuts import render

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
from accounts.models import Usuario
from model.models.Aeropuerto import Aeropuerto

def edicion(request,codigo,tabla,campos):
    email=[]
    if(tabla=="Aeropuerto"):
        elemento = Aeropuerto.objects.get(id=codigo)
    elif(tabla=="Cliente"):
        elemento= Cliente.objects.get(id=codigo)
    elif(tabla=="Nave"):
        elemento= Nave.objects.get(id=codigo)
    elif(tabla=="Vuelo"):
        elemento= Vuelo.objects.get(id=codigo)
    elif(tabla=="Arribo"):
        elemento= Arribo.objects.get(id=codigo)
    elif(tabla=="Instalacion"):
        elemento= Instalacion.objects.get(id=codigo)
    elif(tabla=="Servicio"):
        elemento= Servicio.objects.get(id=codigo)
    elif(tabla=="Valoracion"):
        elemento= Valoracion.objects.get(id=codigo)
    elif(tabla=="Reparacion"):
        elemento= Reparacion.objects.get(id=codigo)
    elif(tabla=="ReparaNave"):
        elemento= ReparaNave.objects.get(id=codigo)
    elif(tabla=="ReparacionesDependientes"):
        elemento= ReparacionesDependientes.objects.get(id=codigo)
    elif(tabla=="Admin_de_Aeropuerto"):
        elemento= Usuario.objects.get(id=codigo)
        aeropuertos=Aeropuerto.objects.all()
        usuarios=Usuario.objects.all()
        for user in usuarios:
            email.append(user.email)
    return render(request, "edicion.html", {"elemento": elemento,"tabla":tabla,"campos":campos,"aeropuertos": aeropuertos,"email":email})

