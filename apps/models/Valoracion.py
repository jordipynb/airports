from django.db import models
from .Servicio import Servicio
from .Arribo import Arribo
class Valoracion(models.Model):
    # El id de esta tabla se oculta, ya hay llave primaria
    # La Referencia a Servicio se oculta ya hay referencia por llave compuesta
    # La Referencia a Arribo se oculta ya hay referencia por llave compuesta
    Id_S = models.ForeignKey(Servicio,verbose_name="ID Servicio",null=False,on_delete=models.CASCADE)
    Id_Ar = models.ForeignKey(Arribo,verbose_name="ID Arribo",null=False,on_delete=models.CASCADE)
    Id_I = models.IntegerField(verbose_name="ID Instalacion",null=False)
    Codigo = models.IntegerField(verbose_name="Codigo",null=False)
    No_Mat = models.CharField(verbose_name="No. Matricula",null=False,max_length=30)
    Fecha_in = models.DateTimeField(verbose_name="Fecha de Entrada",null=False)
    Id_C = models.IntegerField(verbose_name="ID Cliente",null=False)
    Valoracion = models.CharField(verbose_name="Valoracion",max_length=100)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['Id_I','Codigo','No_Mat','Fecha_in','Id_C'],name='Id de Valoracion')]

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id)
    def __iter__(self):
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Servicio": 
                value1=getattr(self,field_name.attname,None)
                servicio = Servicio.objects.get(id=value1)
                continue
            if field_name.verbose_name == "ID Arribo": 
                value2=getattr(self,field_name.attname,None)
                arribo = Arribo.objects.get(id=value2)
                continue
            value=getattr(self,field_name.attname,None)
            if field_name.verbose_name == "ID Instalacion": 
                self.Id_I = str(servicio.Id_I)
                self.save()
                value = self.Id_I
            if field_name.verbose_name == "Codigo": 
                self.Codigo = servicio.Codigo
                self.save()
                value = self.Codigo
            if field_name.verbose_name == "No. Matricula": 
                self.No_Mat = arribo.No_Mat
                self.save()
                value = self.No_Mat
            if field_name.verbose_name == "Fecha de Entrada": 
                self.Fecha_in = arribo.Fecha_in
                self.save()
                value = self.Fecha_in
            if field_name.verbose_name == "ID Cliente": 
                self.Id_C = str(arribo.Id_C)
                self.save()
                value = self.Id_C
            yield value
    def campos(self):
        output=[]
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Servicio": continue
            if field_name.verbose_name == "ID Arribo": continue
            output.append(field_name.verbose_name)
        return output  