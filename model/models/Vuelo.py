from django.db import models
from .Nave import Nave
from .Aeropuerto import Aeropuerto
class Vuelo(models.Model):
    # El id de esta tabla se oculta, ya hay llave primaria
    No_Mat = models.ForeignKey(Nave,verbose_name="No. Matricula",null=False,max_length=30,on_delete=models.CASCADE)
    Fecha_in = models.DateTimeField(verbose_name="Fecha de Entrada",null=False)
    Id_A = models.ForeignKey(Aeropuerto,verbose_name="ID Aeropuerto",null=False,on_delete=models.CASCADE)
    Fecha_out = models.DateTimeField(verbose_name="Fecha de Salida",null=False)
    EstadoNave = models.CharField(verbose_name="Estado",null=False,max_length=50)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['No_Mat','Fecha_in'],name='Id del Vuelo')]

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id)
    def __iter__(self):
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            value=getattr(self,field_name.attname,None)
            if field_name.verbose_name == "No. Matricula": 
                nave = Nave.objects.get(id=value)
                value = nave.No_Mat
            yield value
    def campos(self):
        output=[]
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            output.append(field_name.verbose_name)
        return output