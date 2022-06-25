from django.db import models
from .Aeropuerto import Aeropuerto
class Instalacion(models.Model):
    Nom_I = models.CharField(verbose_name="Nombre",null=False,max_length=40)
    Tipo_I = models.CharField(verbose_name="Tipo",null=False,max_length=50)
    Ubicacion = models.CharField(verbose_name="Ubicacion",max_length=50)
    Id_A = models.ForeignKey(Aeropuerto,verbose_name="ID Aeropuerto",on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id)
    def __iter__(self):
        for field_name in self._meta.fields:
            value=getattr(self,field_name.attname,None)
            yield value
    def campos(self):
        output=[]
        for field_name in self._meta.fields:
            output.append(field_name.verbose_name)
        return output