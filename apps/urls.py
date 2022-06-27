from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('listar/', views.listar),
    path('registrar/', views.registrar),
    path('listar/edicion/<codigo>/<tabla>/<campos>', views.edicion),
    path('editar/', views.editar),
    path('listar/eliminar/<codigo>/<tabla>', views.eliminar),
]
