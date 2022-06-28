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
from accounts.models import Usuario

def editar(request):
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
    total_P = request.POST['Total_P']
    no_MatV = request.POST['No_MatV']
    fecha_inV = request.POST['Fecha_inV']
    fecha_outV = request.POST['Fecha_outV']
    estadoNave = request.POST['EstadoNave']
    no_MatA = request.POST['No_MatA']
    fecha_inA = request.POST['Fecha_inA']
    id_CA = request.POST['Id_CA']
    caracter = request.POST['Caracter']
    nom_I = request.POST['Nom_I']
    tipo_I = request.POST['Tipo_I']
    ubicacion = request.POST['Ubicacion']
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
    admin_de_Aeropuerto_Id_A = request.POST['Admin_de_Aeropuerto_Id_A']
    if data=="Aeropuerto":
        aeropuerto = Aeropuerto.objects.get(id=codigo)
        aeropuerto.Nom_A = nombre
        aeropuerto.Direccion = direccion
        aeropuerto.Pos_Geo = pos_Geo
        aeropuerto.save()
    elif data=="Cliente":
        cliente = Cliente.objects.get(id=codigo)
        cliente.Nom_C = nom_C
        cliente.Tipo_C = tipo_C
        cliente.Nacionalidad = nacionalidad
        cliente.save()
    elif data=="Nave":
        nave = Nave.objects.get(id=codigo)
        nave.No_Mat = no_Mat
        nave.Clasific = clasific
        nave.Capacidad = capacidad
        nave.No_Trip = no_Trip
        nave.Total_P = total_P
        cliente = Cliente.objects.get(id=id_D)
        nave.Id_D=cliente
        nave.save()
    elif data=="Vuelo":
        vuelo = Vuelo.objects.get(id=codigo)
        nave = Nave.objects.get(No_Mat=no_MatV)
        vuelo.No_Mat = nave
        vuelo.Fecha_in = fecha_inV
        vuelo.Fecha_out = fecha_outV
        vuelo.EstadoNave = estadoNave
        vuelo.save()
    elif data=="Arribo":
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
    elif data=="Instalacion":
        instalacion = Instalacion.objects.get(id=codigo)
        instalacion.Nom_I = nom_I
        instalacion.Tipo_I = tipo_I
        instalacion.Ubicacion = ubicacion
        instalacion.save()
    elif data=="Servicio":
        servicio = Servicio.objects.get(id=codigo)
        instalacion = Instalacion.objects.get(id=id_IS)
        servicio.Id_I = instalacion
        servicio.Codigo = codigoS
        servicio.Precio = precio
        servicio.Descripcion = descripcion
        servicio.save()
    elif data=="Valoracion":
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
    elif data=="Reparacion":
        instalacion = Instalacion.objects.get(id=id_IR)
        servicio = Servicio.objects.get(Id_I=instalacion,Codigo=codigoR)
        reparacion = Reparacion.objects.get(id=codigo)
        reparacion.Id_S = servicio
        reparacion.Id_I = id_IR
        reparacion.Codigo = codigoR
        reparacion.Tipo = tipoR
        reparacion.save()
    elif data=="ReparaNave":
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
    elif data=="ReparacionesDependientes":
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
    elif data=="Admin_de_Aeropuerto":
        admin_de_aeropuerto=Usuario.objects.get(id=codigo)
        admin_de_aeropuerto.id_role=admin_de_Aeropuerto_Id_A
        admin_de_aeropuerto.save()
    messages.success(request, 'Actualizado!')
    return redirect('/')

