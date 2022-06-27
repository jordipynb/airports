from django.shortcuts import redirect
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

def registrar(request):   
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
    elif data == "Cliente":
        cliente = Cliente.objects.create(
        Nom_C=nom_C,Tipo_C=tipo_C,Nacionalidad=nacionalidad)
    elif data == "Nave":
        cliente = Cliente.objects.get(id=id_D)
        nave = Nave.objects.create(
        No_Mat=no_Mat,Clasific=clasific,Capacidad=capacidad,No_Trip=no_Trip,Total_P=total_P,Id_D=cliente)
    elif data == "Vuelo":
        nave = Nave.objects.get(No_Mat=no_MatV)
        aeropuerto = Aeropuerto.objects.get(id=id_AV)
        vuelo = Vuelo.objects.create(
        No_Mat=nave,Fecha_in=fecha_inV,Id_A=aeropuerto,Fecha_out=fecha_outV,EstadoNave=estadoNave)
    elif data == "Arribo":
        cliente = Cliente.objects.get(id=id_CA)
        nave = Nave.objects.get(No_Mat=no_MatA)
        vuelo = Vuelo.objects.get(No_Mat=nave,Fecha_in=fecha_inA)
        arribo = Arribo.objects.create(
        Id_V=vuelo,No_Mat=no_MatA,Fecha_in=fecha_inA,Id_C=cliente,Caracter=caracter)
    elif data == "Instalacion":
        aeropuerto = Aeropuerto.objects.get(id=id_AI)
        instalacion = Instalacion.objects.create(
        Nom_I=nom_I,Tipo_I=tipo_I,Ubicacion=ubicacion,Id_A=aeropuerto)
    elif data == "Servicio":
        instalacion = Instalacion.objects.get(id=id_IS)
        servicio = Servicio.objects.create(
        Id_I=instalacion,Codigo=codigoS,Precio=precio,Descripcion=descripcion)
    elif data == "Valoracion":
        instalacion = Instalacion.objects.get(id=id_IV)
        servicio = Servicio.objects.get(Id_I=instalacion,Codigo=codigoV)
        cliente = Cliente.objects.get(id=id_CV)
        arribo = Arribo.objects.get(No_Mat=no_MatVal,Fecha_in=fecha_inVal,Id_C=cliente)
        valoracion = Valoracion.objects.create(
        Id_S=servicio,Id_Ar=arribo,Id_I=id_IV,Codigo=codigoV,No_Mat=no_MatVal,Fecha_in=fecha_inVal,Id_C=id_CV,Valoracion=valoracionV)
    elif data == "Reparacion":
        instalacion = Instalacion.objects.get(id=id_IR)
        servicio = Servicio.objects.get(Id_I=instalacion,Codigo=codigoR)
        reparacion = Reparacion.objects.create(
        Id_S=servicio,Id_I=id_IR,Codigo=codigoR,Tipo=tipoR)
    elif data == "ReparaNave":
        reparacion = Reparacion.objects.get(Id_I=id_IRN,Codigo=codigoRN,Tipo=tipoRN)
        nave = Nave.objects.get(No_Mat=no_MatRN)
        vuelo = Vuelo.objects.get(No_Mat=nave,Fecha_in=fecha_inRN)
        reparanave = ReparaNave.objects.create(
        Id_Rep=reparacion,Id_V=vuelo,Id_I=id_IRN,Codigo=codigoRN,Tipo=tipoRN,No_Mat=no_MatRN,Fecha_in=fecha_inRN,Fecha_Ini=fecha_Ini,Tiempo_P=tiempo_P,Fecha_Fin=fecha_Fin)
    elif data == "ReparacionesDependientes":
        reparacion1 = Reparacion.objects.get(Id_I=id_IRD,Codigo=codigoRD,Tipo=tipoRD)
        reparacion2 = Reparacion.objects.get(Id_I=id_IRDD,Codigo=codigoRDD,Tipo=tipoRDD)
        reparacionesDependientes = ReparacionesDependientes.objects.create(
        Id_Rep=reparacion1,Id_RepDep=reparacion2,Id_I=id_IRD,Codigo=codigoRD,Tipo=tipoRD,Id_IDep=id_IRDD,Codigo_Dep=codigoRDD,Tipo_Dep=tipoRDD)
    messages.success(request, 'Registrado!')
    return redirect('/')

