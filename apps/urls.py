from django.urls import path, re_path
from apps import views
from .views.home import home
from .views.listar import listar
from .views.registrar import registrar
from .views.edicion import edicion
from .views.editar import editar
from .views.eliminar import eliminar
from authn.views import register
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', home),
    path('listar/', listar),
    path('registrar/', registrar),
    path('listar/edicion/<codigo>/<tabla>/<campos>', edicion),
    path('editar/', editar),
    path('listar/eliminar/<codigo>/<tabla>', eliminar),
    path('register/', register, name='register'),
    path('snd_consulta/', views.home.snd_consulta),
    path('reparaciones/', views.home.reparaciones),
    path('first_consult/', views.home.first_consult),
    path('third_consult/', views.home.third_consult),
    path('reparaciones_ineficientes/', views.home.reparaciones_ineficientes),
    ]
