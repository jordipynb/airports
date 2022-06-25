from django.db import models
from .Plazas import Plazas
from .Cliente import Cliente
class Nave(models.Model):
    No_Mat = models.CharField(verbose_name="No. Matricula",null=False,unique=True,max_length=30)
    Clasific = models.CharField(verbose_name="Clasificacion",null=False,max_length=50)
    Capacidad = models.SmallIntegerField(verbose_name="Capacidad",null=False)
    No_Trip = models.SmallIntegerField(verbose_name="No. Tripulantes",null=False)
    # Este ID queda oculto
    Id_Plazas = models.ForeignKey(Plazas,verbose_name='ID Plazas',on_delete=models.CASCADE)
    Id_D = models.ForeignKey(Cliente, verbose_name="ID Dueño",null=False,on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.No_Mat)
    def __iter__(self):
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Plazas": continue
            value=getattr(self,field_name.attname,None)
            yield value
    def campos(self):
        output=[]
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Plazas": continue
            output.append(field_name.verbose_name)
        return output