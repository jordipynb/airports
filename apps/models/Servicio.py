from django.db import models
from .Instalacion import Instalacion
class Servicio(models.Model):
    # El id de esta tabla se oculta, ya hay llave primaria
    Id_I = models.ForeignKey(Instalacion,verbose_name="ID Instalacion",null=False,on_delete=models.CASCADE)
    Codigo = models.IntegerField(verbose_name="Codigo",null=False)
    Precio = models.FloatField(verbose_name="Precio",null=False)
    Descripcion = models.CharField(verbose_name="Descripcion",max_length=250)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['Id_I','Codigo'],name='Id del Servicio')]

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id)
    def __iter__(self):
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            value=getattr(self,field_name.attname,None)
            yield value
    def campos(self):
        output=[]
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            output.append(field_name.verbose_name)
        return output  