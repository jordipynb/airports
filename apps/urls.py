from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('listar/', views.listar),
    path('registrarAeropuerto/', views.registrarAeropuerto),
    path('listar/edicionAeropuerto/<codigo>/<tabla>/<campos>', views.edicionAeropuerto),
    path('editarAeropuerto/', views.editarAeropuerto),
    path('listar/eliminarAeropuerto/<codigo>/<tabla>', views.eliminarAeropuerto),
]