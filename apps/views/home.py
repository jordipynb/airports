from django.shortcuts import render
from model.models import ReparaNave
from model.models import Reparacion
from model.models import Arribo
from model.models import Servicio
from model.models import Valoracion
from model.models.Aeropuerto import Aeropuerto
from model.models.Cliente import Cliente
from model.models.Nave import Nave
from accounts.models import Usuario
from model.models.Vuelo import Vuelo
from django.contrib.auth import get_user
from model.models.Instalacion import Instalacion
from django.db.models import F
from django.db.models import Max, Count, Avg, Subquery, OuterRef
import datetime


def home(request):
    email = []
    aeropuertos = Aeropuerto.objects.all()
    clientes = Cliente.objects.all()
    naves = Nave.objects.all()
    vuelos = Vuelo.objects.all()
    usuarios = Usuario.objects.filter(role="US")
    user = get_user(request)
    instalaciones = []
    if user.is_authenticated:
        id = user.id_role
        curretnt_inst = Instalacion.objects.filter(Id_A=id)
        for i in curretnt_inst:
            instalaciones.append(i.id)
    for user in usuarios:
        email.append(user.email)
    return render(request, "gestion.html",
                  {"aeropuertos": aeropuertos, "email": email, "instalaciones": instalaciones, "naves": naves,
                   "clientes": clientes, "vuelos": vuelos})


def snd_consulta(request):
    consulta = (Arribo.Arribo.objects.filter(Id_V__No_Mat__Id_D=F('Id_C'), Caracter='capitan',
                                             Id_V__Id_A__Nom_A='Jose Marti').select_related('Id_C')).values_list(
        'Id_C__Nom_C', 'Id_C__Tipo_C').order_by('Id_C__Tipo_C')
    campos = ['Nombre', 'Tipo']
    return render(request, "listados.html", {"campos": campos, "aeropuertos": consulta, "tabla": ""})


def reparaciones(request):
    consulta = ReparaNave.ReparaNave.objects.select_related('Id_V').values('Id_V__Id_A').annotate(
        cantidad=Count('id')).values_list('Id_V__Id_A', 'cantidad')
    campos = ['Aeropuerto', 'Cantidad de Reparaciones']
    return render(request, "listados.html", {"campos": campos, "aeropuertos": consulta, "tabla": ""})


def first_consult(request):
    consulta = Reparacion.Reparacion.objects.select_related('Id_I').values('Id_S__Id_I__Id_A').annotate(
        cantidad=Count('id')).values_list('Id_S__Id_I__Id_A__Nom_A', 'Id_S__Id_I__Id_A__Pos_Geo')
    campos = ['Nombre', 'Posicion Geografica']
    return render(request, "listados.html", {"campos": campos, "aeropuertos": consulta, "tabla": ""})


def third_consult(request):
    # consulta=Vuelo.objects.filter(Fecha_in__year__gt=2010).values('Id_A').annotate(cantidad=Count('id')).values('cantidad').annotate(total=Count('id')).order_by('-cantidad').values_list('Id_A','cantidad')
    consulta = Vuelo.objects.filter(
        Fecha_in__year__gt=2010).values(
        'Id_A').annotate(
        cantidad=Count('id'), cant_servicios=Subquery(
            Servicio.Servicio.objects.select_related(
                'Id_I').filter(
                Id_I__Id_A=OuterRef('Id_A')).values(
                'Id_I__Id_A').annotate(
                servicios=Count('id')).values('servicios')))

    consulta1 = consulta.aggregate(max=Max('cantidad'))
    max = consulta1['max']
    consulta_final = consulta.filter(cantidad=max).values_list('Id_A__Nom_A', 'cant_servicios')
    campos = ['Nombre de Aeropuerto', 'Cantidad de Servicios']
    return render(request, "listados.html", {"campos": campos, "aeropuertos": consulta_final, "tabla": ""})


def reparaciones_ineficientes(request):
    consulta = (ReparaNave.ReparaNave.objects.filter(
        Id_Rep__Id_S__Id_I__Id_A__Nom_A='Jose Marti')).filter(
        Fecha_Fin__gt=F('Tiempo_P')).filter(
        Fecha_Ini__year=datetime.date.today().year - 1).values('Id_Rep').annotate(monto=Avg('Id_Rep__Id_S__Precio'),
                                                                                  valoracion_promedio=Subquery(
                                                                                      Valoracion.Valoracion.objects.filter(
                                                                                          Id_Ar__Id_V__Id_A=OuterRef(
                                                                                              'Id_Rep__Id_S__Id_I__Id_A'),
                                                                                          Id_S=OuterRef(
                                                                                              'Id_Rep__Id_S')).annotate(
                                                                                          promedio=Avg(
                                                                                              'Valoracion')).values(
                                                                                          'promedio')
                                                                                  )).filter(
        valoracion_promedio=5).values_list('Id_Rep__Id_S', 'monto')
    campos = ['Servicio', 'Monto']
    return render(request, "listados.html", {"campos": campos, "aeropuertos": consulta, "tabla": ""})
