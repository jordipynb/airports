from django.shortcuts import render
from model.models.Aeropuerto import Aeropuerto
from accounts.models import Usuario
def home(request):
    email=[]
    aeropuertos = Aeropuerto.objects.all()
    usuarios= Usuario.objects.all()
    aeropuertos=Aeropuerto.objects.all()
    for user in usuarios:
        email.append(user.email)
    return render(request, "gestion.html",{"aeropuertos": aeropuertos,"email":email})
