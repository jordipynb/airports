from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

def listar(request):
    dict=para_listar(request)
    return render(request, "listados.html", dict)

def para_listar(request):
    data = request.POST['data']
    listado=[]
    if data == "Aeropuerto":
        listado = Aeropuerto.objects.all()
    if data == "Cliente":
        listado = Cliente.objects.all()
    if data == "Nave":
        listado = Nave.objects.all()
    if data == "Plazas":
        listado = Plazas.objects.all()
    if data == "Vuelo":
        listado = Vuelo.objects.all()
    if data == "Arribo":
        listado = Arribo.objects.all()
    if data == "Instalacion":
        listado = Instalacion.objects.all()
    if data == "Servicio":
        listado = Servicio.objects.all()
    if data == "Valoracion":
        listado = Valoracion.objects.all()
    if data == "Reparacion":
        listado = Reparacion.objects.all()
    if data == "ReparaNave":
        listado = ReparaNave.objects.all()
    if data == "ReparacionesDependientes":
        listado = ReparacionesDependientes.objects.all()
    messages.success(request, 'Listados!')
    campos=[]
    for a in listado:
        campos=a.campos()
        break
    return {"campos": campos,"aeropuertos": listado,"tabla":data}

def home(request):
    return render(request, "gestionar_aeropuertos.html")

def registrarAeropuerto(request):   
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    pos_Geo = request.POST['pos_Geo']
    nom_C = request.POST['Nom_C']
    tipo_C = request.POST['Tipo_C']
    nacionalidad = request.POST['Nacionalidad']
    data = request.POST['data']
    no_Mat = request.POST['No_Mat']
    clasific = request.POST['Clasific']
    capacidad = request.POST['Capacidad']
    no_Trip = request.POST['No_Trip']
    id_D = request.POST['Id_D']
    clasificP = request.POST['ClasificP']
    capacidadP = request.POST['CapacidadP']
    no_TripP = request.POST['No_TripP']
    total_P = request.POST['Total_P']
    no_MatV = request.POST['No_MatV']
    fecha_inV = request.POST['Fecha_inV']
    id_AV = request.POST['Id_AV']
    fecha_outV = request.POST['Fecha_outV']
    estadoNave = request.POST['EstadoNave']
    no_MatA = request.POST['No_MatA']
    fecha_inA = request.POST['Fecha_inA']
    id_CA = request.POST['Id_CA']
    caracter = request.POST['Caracter']
    nom_I = request.POST['Nom_I']
    tipo_I = request.POST['Tipo_I']
    ubicacion = request.POST['Ubicacion']
    id_AI = request.POST['Id_AI']
    id_IS = request.POST['Id_IS']
    codigoS = request.POST['CodigoS']
    precio = request.POST['Precio']
    descripcion = request.POST['Descripcion']
    id_IV = request.POST['Id_IV']
    codigoV = request.POST['CodigoV']
    no_MatVal = request.POST['No_MatVal']
    fecha_inVal = request.POST['Fecha_inVal']
    id_CV = request.POST['Id_CV']
    valoracionV = request.POST['ValoracionV']
    id_IR = request.POST['Id_IR']
    codigoR = request.POST['CodigoR']
    tipoR = request.POST['TipoR']
    id_IRN = request.POST['Id_IRN']
    codigoRN = request.POST['CodigoRN']
    tipoRN = request.POST['TipoRN']
    no_MatRN = request.POST['No_MatRN']
    fecha_inRN = request.POST['Fecha_inRN']
    fecha_Ini = request.POST['Fecha_Ini']
    tiempo_P = request.POST['Tiempo_P']
    fecha_Fin = request.POST['Fecha_Fin']
    id_IRD = request.POST['Id_IRD']
    codigoRD = request.POST['CodigoRD']
    tipoRD = request.POST['TipoRD']
    id_IRDD = request.POST['Id_IRDD']
    codigoRDD = request.POST['CodigoRDD']
    tipoRDD = request.POST['TipoRDD']
    if data == "Aeropuerto":
        aeropuerto = Aeropuerto.objects.create(
        Nom_A=nombre,Direccion=direccion,Pos_Geo=pos_Geo)
    if data == "Cliente":
        cliente = Cliente.objects.create(
        Nom_C=nom_C,Tipo_C=tipo_C,Nacionalidad=nacionalidad)
    if data == "Nave":
        cliente = Cliente.objects.get(id=id_D)
        plazas = Plazas.objects.get(Clasific=clasific, No_Trip=no_Trip, Capacidad=capacidad)
        nave = Nave.objects.create(
        No_Mat=no_Mat,Clasific=clasific,Capacidad=capacidad,No_Trip=no_Trip,Id_D=cliente,Id_Plazas=plazas)
    if data == "Plazas":
        plazas = Plazas.objects.create(
        Clasific=clasificP,No_Trip=no_TripP,Capacidad=capacidadP,Total_P=total_P)
    if data == "Vuelo":
        nave = Nave.objects.get(No_Mat=no_MatV)
        aeropuerto = Aeropuerto.objects.get(id=id_AV)
        vuelo = Vuelo.objects.create(
        No_Mat=nave,Fecha_in=fecha_inV,Id_A=aeropuerto,Fecha_out=fecha_outV,EstadoNave=estadoNave)
    if data == "Arribo":
        cliente = Cliente.objects.get(id=id_CA)
        nave = Nave.objects.get(No_Mat=no_MatA)
        vuelo = Vuelo.objects.get(No_Mat=nave,Fecha_in=fecha_inA)
        arribo = Arribo.objects.create(
        Id_V=vuelo,No_Mat=no_MatA,Fecha_in=fecha_inA,Id_C=cliente,Caracter=caracter)
    if data == "Instalacion":
        aeropuerto = Aeropuerto.objects.get(id=id_AI)
        instalacion = Instalacion.objects.create(
        Nom_I=nom_I,Tipo_I=tipo_I,Ubicacion=ubicacion,Id_A=aeropuerto)
    if data == "Servicio":
        instalacion = Instalacion.objects.get(id=id_IS)
        servicio = Servicio.objects.create(
        Id_I=instalacion,Codigo=codigoS,Precio=precio,Descripcion=descripcion)
    if data == "Valoracion":
        instalacion = Instalacion.objects.get(id=id_IV)
        servicio = Servicio.objects.get(Id_I=instalacion,Codigo=codigoV)
        cliente = Cliente.objects.get(id=id_CV)
        arribo = Arribo.objects.get(No_Mat=no_MatVal,Fecha_in=fecha_inVal,Id_C=cliente)
        valoracion = Valoracion.objects.create(
        Id_S=servicio,Id_Ar=arribo,Id_I=id_IV,Codigo=codigoV,No_Mat=no_MatVal,Fecha_in=fecha_inVal,Id_C=id_CV,Valoracion=valoracionV)
    if data == "Reparacion":
        instalacion = Instalacion.objects.get(id=id_IR)
        servicio = Servicio.objects.get(Id_I=instalacion,Codigo=codigoR)
        reparacion = Reparacion.objects.create(
        Id_S=servicio,Id_I=id_IR,Codigo=codigoR,Tipo=tipoR)
    if data == "ReparaNave":
        reparacion = Reparacion.objects.get(Id_I=id_IRN,Codigo=codigoRN,Tipo=tipoRN)
        nave = Nave.objects.get(No_Mat=no_MatRN)
        vuelo = Vuelo.objects.get(No_Mat=nave,Fecha_in=fecha_inRN)
        reparanave = ReparaNave.objects.create(
        Id_Rep=reparacion,Id_V=vuelo,Id_I=id_IRN,Codigo=codigoRN,Tipo=tipoRN,No_Mat=no_MatRN,Fecha_in=fecha_inRN,Fecha_Ini=fecha_Ini,Tiempo_P=tiempo_P,Fecha_Fin=fecha_Fin)
    if data == "ReparacionesDependientes":
        reparacion1 = Reparacion.objects.get(Id_I=id_IRD,Codigo=codigoRD,Tipo=tipoRD)
        reparacion2 = Reparacion.objects.get(Id_I=id_IRDD,Codigo=codigoRDD,Tipo=tipoRDD)
        reparacionesDependientes = ReparacionesDependientes.objects.create(
        Id_Rep=reparacion1,Id_RepDep=reparacion2,Id_I=id_IRD,Codigo=codigoRD,Tipo=tipoRD,Id_IDep=id_IRDD,Codigo_Dep=codigoRDD,Tipo_Dep=tipoRDD)
    messages.success(request, 'Registrado!')
    return redirect('/')

def editarAeropuerto(request):
    codigo = request.POST['id']
    nombre = request.POST['nombre']
    direccion = request.POST['direccion']
    pos_Geo = request.POST['pos_Geo']
    nom_C = request.POST['Nom_C']
    tipo_C = request.POST['Tipo_C']
    nacionalidad = request.POST['Nacionalidad']
    data = request.POST['tabla']
    no_Mat = request.POST['No_Mat']
    clasific = request.POST['Clasific']
    capacidad = request.POST['Capacidad']
    no_Trip = request.POST['No_Trip']
    id_D = request.POST['Id_D']
    clasificP = request.POST['ClasificP']
    capacidadP = request.POST['CapacidadP']
    no_TripP = request.POST['No_TripP']
    total_P = request.POST['Total_P']
    no_MatV = request.POST['No_MatV']
    fecha_inV = request.POST['Fecha_inV']
    id_AV = request.POST['Id_AV']
    fecha_outV = request.POST['Fecha_outV']
    estadoNave = request.POST['EstadoNave']
    no_MatA = request.POST['No_MatA']
    fecha_inA = request.POST['Fecha_inA']
    id_CA = request.POST['Id_CA']
    caracter = request.POST['Caracter']
    nom_I = request.POST['Nom_I']
    tipo_I = request.POST['Tipo_I']
    ubicacion = request.POST['Ubicacion']
    id_AI = request.POST['Id_AI']
    id_IS = request.POST['Id_IS']
    codigoS = request.POST['CodigoS']
    precio = request.POST['Precio']
    descripcion = request.POST['Descripcion']
    id_IV = request.POST['Id_IV']
    codigoV = request.POST['CodigoV']
    no_MatVal = request.POST['No_MatVal']
    fecha_inVal = request.POST['Fecha_inVal']
    id_CV = request.POST['Id_CV']
    valoracionV = request.POST['ValoracionV']
    id_IR = request.POST['Id_IR']
    codigoR = request.POST['CodigoR']
    tipoR = request.POST['TipoR']
    id_IRN = request.POST['Id_IRN']
    codigoRN = request.POST['CodigoRN']
    tipoRN = request.POST['TipoRN']
    no_MatRN = request.POST['No_MatRN']
    fecha_inRN = request.POST['Fecha_inRN']
    fecha_Ini = request.POST['Fecha_Ini']
    tiempo_P = request.POST['Tiempo_P']
    fecha_Fin = request.POST['Fecha_Fin']
    id_IRD = request.POST['Id_IRD']
    codigoRD = request.POST['CodigoRD']
    tipoRD = request.POST['TipoRD']
    id_IRDD = request.POST['Id_IRDD']
    codigoRDD = request.POST['CodigoRDD']
    tipoRDD = request.POST['TipoRDD']
    if data=="Aeropuerto":
        aeropuerto = Aeropuerto.objects.get(id=codigo)
        aeropuerto.Nom_A = nombre
        aeropuerto.Direccion = direccion
        aeropuerto.Pos_Geo = pos_Geo
        aeropuerto.save()
    if data=="Cliente":
        cliente = Cliente.objects.get(id=codigo)
        cliente.Nom_C = nom_C
        cliente.Tipo_C = tipo_C
        cliente.Nacionalidad = nacionalidad
        cliente.save()
    if data=="Nave":
        nave = Nave.objects.get(id=codigo)
        nave.No_Mat = no_Mat
        nave.Clasific = clasific
        nave.Capacidad = capacidad
        nave.No_Trip = no_Trip
        plazas = Plazas.objects.get(Clasific=clasific, No_Trip=no_Trip, Capacidad=capacidad)
        nave.Id_Plazas = plazas
        cliente = Cliente.objects.get(id=id_D)
        nave.Id_D=cliente
        nave.save()
    if data=="Plazas":
        plazas = Plazas.objects.get(id=codigo)
        plazas.Clasific = clasificP
        plazas.No_Trip = no_TripP
        plazas.Capacidad = capacidadP
        plazas.Total_P = total_P
        plazas.save()
    if data=="Vuelo":
        vuelo = Vuelo.objects.get(id=codigo)
        nave = Nave.objects.get(No_Mat=no_MatV)
        aeropuerto = Aeropuerto.objects.get(id=id_AV)
        vuelo.No_Mat = nave
        vuelo.Fecha_in = fecha_inV
        vuelo.Id_A = aeropuerto
        vuelo.Fecha_out = fecha_outV
        vuelo.EstadoNave = estadoNave
        vuelo.save()
    if data=="Arribo":
        arribo = Arribo.objects.get(id=codigo)
        cliente = Cliente.objects.get(id=id_CA)
        nave = Nave.objects.get(No_Mat=no_MatA)
        vuelo = Vuelo.objects.get(No_Mat=nave,Fecha_in=fecha_inA) 
        arribo.Id_V = vuelo
        arribo.No_Mat = no_MatA
        arribo.Fecha_in = fecha_inA
        arribo.Id_C = cliente
        arribo.Caracter = caracter
        arribo.save()
    if data=="Instalacion":
        instalacion = Instalacion.objects.get(id=codigo)
        aeropuerto = Aeropuerto.objects.get(id=id_AI)
        instalacion.Id_A = aeropuerto
        instalacion.Nom_I = nom_I
        instalacion.Tipo_I = tipo_I
        instalacion.Ubicacion = ubicacion
        instalacion.save()
    if data=="Servicio":
        servicio = Servicio.objects.get(id=codigo)
        instalacion = Instalacion.objects.get(id=id_IS)
        servicio.Id_I = instalacion
        servicio.Codigo = codigoS
        servicio.Precio = precio
        servicio.Descripcion = descripcion
        servicio.save()
    if data=="Valoracion":
        instalacion = Instalacion.objects.get(id=id_IV)
        servicio = Servicio.objects.get(Id_I=instalacion,Codigo=codigoV)
        cliente = Cliente.objects.get(id=id_CV)
        arribo = Arribo.objects.get(No_Mat=no_MatVal,Fecha_in=fecha_inVal,Id_C=cliente)
        valoracion = Valoracion.objects.get(id=codigo)
        valoracion.Id_S = servicio
        valoracion.Id_Ar = arribo
        valoracion.Id_I = id_IV
        valoracion.Codigo = codigoV
        valoracion.No_Mat = no_MatVal
        valoracion.Fecha_in = fecha_inVal
        valoracion.Id_C = id_CV
        valoracion.Valoracion = valoracionV
        valoracion.save()
    if data=="Reparacion":
        instalacion = Instalacion.objects.get(id=id_IR)
        servicio = Servicio.objects.get(Id_I=instalacion,Codigo=codigoR)
        reparacion = Reparacion.objects.get(id=codigo)
        reparacion.Id_S = servicio
        reparacion.Id_I = id_IR
        reparacion.Codigo = codigoR
        reparacion.Tipo = tipoR
        reparacion.save()
    if data=="ReparaNave":
        reparacion = Reparacion.objects.get(Id_I=id_IRN,Codigo=codigoRN,Tipo=tipoRN)
        nave = Nave.objects.get(No_Mat=no_MatRN)
        vuelo = Vuelo.objects.get(No_Mat=nave,Fecha_in=fecha_inRN)
        reparanave = ReparaNave.objects.get(id=codigo)
        reparanave.Id_Rep = reparacion
        reparanave.Id_V = vuelo
        reparanave.Id_I = id_IRN
        reparanave.Codigo = codigoRN
        reparanave.Tipo = tipoRN
        reparanave.No_Mat = no_MatRN
        reparanave.Fecha_in = fecha_inRN
        reparanave.Fecha_Ini = fecha_Ini
        reparanave.Tiempo_P = tiempo_P
        reparanave.Fecha_Fin = fecha_Fin
        reparanave.save()
    if data=="ReparacionesDependientes":
        reparacion1 = Reparacion.objects.get(Id_I=id_IRD,Codigo=codigoRD,Tipo=tipoRD)
        reparacion2 = Reparacion.objects.get(Id_I=id_IRDD,Codigo=codigoRDD,Tipo=tipoRDD)
        reparacionesDependientes = ReparacionesDependientes.objects.get(id=codigo)
        reparacionesDependientes.Id_Rep = reparacion1
        reparacionesDependientes.Id_RepDep = reparacion2
        reparacionesDependientes.Id_I = id_IRD
        reparacionesDependientes.Codigo = codigoRD
        reparacionesDependientes.Tipo = tipoRD
        reparacionesDependientes.Id_IDep = id_IRDD
        reparacionesDependientes.Codigo_Dep = codigoRDD
        reparacionesDependientes.Tipo_Dep = tipoRDD 
        reparacionesDependientes.save()
    messages.success(request, 'Actualizado!')
    return redirect('/')

def edicionAeropuerto(request,codigo,tabla,campos):
    if(tabla=="Aeropuerto"):
        elemento = Aeropuerto.objects.get(id=codigo)
    if(tabla=="Cliente"):
        elemento= Cliente.objects.get(id=codigo)
    if(tabla=="Nave"):
        elemento= Nave.objects.get(id=codigo)
    if(tabla=="Plazas"):
        elemento= Plazas.objects.get(id=codigo)
    if(tabla=="Vuelo"):
        elemento= Vuelo.objects.get(id=codigo)
    if(tabla=="Arribo"):
        elemento= Arribo.objects.get(id=codigo)
    if(tabla=="Instalacion"):
        elemento= Instalacion.objects.get(id=codigo)
    if(tabla=="Servicio"):
        elemento= Servicio.objects.get(id=codigo)
    if(tabla=="Valoracion"):
        elemento= Valoracion.objects.get(id=codigo)
    if(tabla=="Reparacion"):
        elemento= Reparacion.objects.get(id=codigo)
    if(tabla=="ReparaNave"):
        elemento= ReparaNave.objects.get(id=codigo)
    if(tabla=="ReparacionesDependientes"):
        elemento= ReparacionesDependientes.objects.get(id=codigo)
    return render(request, "edicion_de_aeropuertos.html", {"elemento": elemento,"tabla":tabla,"campos":campos})

def eliminarAeropuerto(request,codigo,tabla):
    if tabla== "Aeropuerto":
        elemento = Aeropuerto.objects.get(id=codigo)
        elemento.delete()
    if tabla== "Cliente":
        elemento = Cliente.objects.get(id=codigo)
        elemento.delete()
    if tabla== "Nave":
        elemento = Nave.objects.get(id=codigo)
        elemento.delete()
    if tabla== "Plazas":
        elemento = Plazas.objects.get(id=codigo)
        elemento.delete()
    if tabla== "Vuelo":
        elemento = Vuelo.objects.get(id=codigo)
        elemento.delete()
    if tabla== "Arribo":
        elemento= Arribo.objects.get(id=codigo)
        elemento.delete()
    if tabla== "Instalacion":
        elemento= Instalacion.objects.get(id=codigo)
        elemento.delete()
    if tabla== "Servicio":
        elemento= Servicio.objects.get(id=codigo)
        elemento.delete()
    if tabla== "Valoracion":
        elemento= Valoracion.objects.get(id=codigo)
        elemento.delete()
    if tabla== "Reparacion":
        elemento= Reparacion.objects.get(id=codigo)
        elemento.delete()
    if tabla== "ReparaNave":
        elemento= ReparaNave.objects.get(id=codigo)
        elemento.delete()
    if tabla== "ReparacionesDependientes":
        elemento= ReparacionesDependientes.objects.get(id=codigo)
        elemento.delete()
    messages.success(request, '¡Eliminado!')
    return redirect('/')