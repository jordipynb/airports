from django.urls import path, re_path
from apps import views
from .views.home import home
from .views.listar import listar
from .views.listar import export_pdf2
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
    path('snd_consulta/', views.listar.snd_consulta),
    path('reparaciones/', views.listar.reparaciones),
    path('first_consult/', views.listar.first_consult),
    path('third_consult/', views.listar.third_consult),
    path('reparaciones_ineficientes/', views.listar.reparaciones_ineficientes),
    path('export/', export_pdf2, name="export-pdf"),
]
