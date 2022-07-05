from django.shortcuts import render
from accounts.models import Usuario
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
from django.http import HttpResponse
from django.template.loader import render_to_string
import pdfkit
from django.db.models import F
from django.db.models import Max, Count, Avg, Subquery, OuterRef
import datetime


def export_pdf2(request):
    html = render_to_string("listados.html", dict1, request)
    css = 'apps/static/css/gestionAeropuerto.css'

    try:
        myPDF = pdfkit.from_string(html, 'report.pdf', css=css)
    except Exception as e:
        temp = open('report.pdf', 'rb')
        response = HttpResponse(temp, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="report.pdf"'
        return response

    response = HttpResponse(myPDF, content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'

    return response


def listar(request):
    global dict1
    dict1 = para_listar(request)
    return render(request, "listados.html", dict1)


def para_listar(request):
    data = str(request.GET['data'])
    listado = []
    name = ""
    if data == "Aeropuerto":
        listado = Aeropuerto.objects.all()
        name = "Aeropuertos"
    elif data == "Cliente":
        listado = Cliente.objects.all()
        name = "Clientes"
    elif data == "Nave":
        listado = Nave.objects.all()
        name = "Naves"
    elif data == "Vuelo":
        listado = Vuelo.objects.all()
        name = "Vuelos"
    elif data == "Arribo":
        listado = Arribo.objects.all()
        name = "Arribos"
    elif data == "Instalacion":
        listado = Instalacion.objects.all()
        name = "Instalaciones"
    elif data == "Servicio":
        listado = Servicio.objects.all()
        name = "Servicios"
    elif data == "Valoracion":
        listado = Valoracion.objects.all()
        name = "Valoraciones"
    elif data == "Reparacion":
        listado = Reparacion.objects.all()
        name = "Reparaciones"
    elif data == "ReparaNave":
        listado = ReparaNave.objects.all()
        name = "Reparaciones de Naves"
    elif data == "ReparacionesDependientes":
        listado = ReparacionesDependientes.objects.all()
        name = "Reparaciones Dependientes"
    elif data == "Admin_de_Aeropuerto":
        listado = Usuario.objects.filter(role="AA")
        name = "Administradores de Aeropuertos"
    elif data == "Admin_de_Instalacion":
        listado = Usuario.objects.filter(role="AI")
        name = "Administradores de Instalaciones"
    # messages.success(request, 'Listados!')
    campos = []
    for a in listado:
        campos = a.campos()
        break
    print(len(campos))

    return {"campos": campos, "aeropuertos": listado, "tabla": data, "name": name}


# Consulta 3
def snd_consulta(request):
    consulta = (Arribo.objects.filter(Id_V__No_Mat__Id_D=F('Id_C'), Caracter='capitan',
                                      Id_V__Id_A__Nom_A='Jose Marti').select_related('Id_C')).values_list(
        'Id_C__Nom_C', 'Id_C__Tipo_C').order_by('Id_C__Tipo_C')
    campos = ['Nombre', 'Tipo']
    global dict1
    dict1 = {"campos": campos, "aeropuertos": consulta, "tabla": "", "name": "Capitanes del Aeropuerto JM"}
    return render(request, "listados.html", dict1)


# Consulta 2
def reparaciones(request):
    consulta = ReparaNave.objects.select_related('Id_V').values('Id_V__Id_A').annotate(
        cantidad=Count('id')).values_list('Id_V__Id_A', 'cantidad')
    campos = ['Aeropuerto', 'Cantidad de Reparaciones']
    global dict1
    dict1 = {"campos": campos, "aeropuertos": consulta, "tabla": "", "name": "Reparaciones Capitales"}
    return render(request, "listados.html", dict1)


# Consulta 1
def first_consult(request):
    consulta = Reparacion.objects.select_related('Id_I').values('Id_S__Id_I__Id_A').annotate(
        cantidad=Count('id')).values_list('Id_S__Id_I__Id_A__Nom_A', 'Id_S__Id_I__Id_A__Pos_Geo')
    campos = ['Nombre', 'Posicion Geografica']
    global dict1
    dict1 = {"campos": campos, "aeropuertos": consulta, "tabla": "", "name": "Aeropuertos con Reparacion"}
    return render(request, "listados.html", dict1)


# Consulta 4
def third_consult(request):
    consulta = Vuelo.objects.filter(
        Fecha_in__year__gt=2010).values(
        'Id_A').annotate(
        cantidad=Count('id'), cant_servicios=Subquery(
            Servicio.objects.select_related(
                'Id_I').filter(
                Id_I__Id_A=OuterRef('Id_A')).values(
                'Id_I__Id_A').annotate(
                servicios=Count('id')).values('servicios')))

    consulta1 = consulta.aggregate(max=Max('cantidad'))
    max = consulta1['max']
    consulta_final = consulta.filter(cantidad=max).values_list('Id_A__Nom_A', 'cant_servicios')
    campos = ['Nombre de Aeropuerto', 'Cantidad de Servicios']
    global dict1
    dict1 = {"campos": campos, "aeropuertos": consulta_final, "tabla": "", "name": "Aeropuertos con Servicios Posteriores a 2010"}
    return render(request, "listados.html", dict1)


# Consulta 5
def reparaciones_ineficientes(request):
    consulta = (ReparaNave.objects.filter(
        Id_Rep__Id_S__Id_I__Id_A__Nom_A='Jose Marti')).filter(
        Fecha_Fin__gt=F('Tiempo_P')).filter(
        Fecha_Ini__year=datetime.date.today().year - 1).values('Id_Rep').annotate(monto=Avg('Id_Rep__Id_S__Precio'),
                                                                                  valoracion_promedio=Subquery(
                                                                                      Valoracion.objects.filter(
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
    global dict1
    dict1 = {"campos": campos, "aeropuertos": consulta, "tabla": "", "name": "Reparaciones Ineficientes"}
    return render(request, "listados.html", dict1)
