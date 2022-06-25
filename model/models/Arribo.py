from django.db import models
from .Vuelo import Vuelo
from .Cliente import Cliente
class Arribo(models.Model):
    # El id de esta tabla se oculta, ya hay llave primaria
    # La Referencia a Vuelo se oculta ya hay referencia por llave compuesta
    Id_V = models.ForeignKey(Vuelo,verbose_name="ID Vuelo",null=False,on_delete=models.CASCADE)
    No_Mat = models.CharField(verbose_name="No. Matricula",null=False,max_length=30)
    Fecha_in = models.DateTimeField(verbose_name="Fecha de Entrada",null=False)
    Id_C = models.ForeignKey(Cliente,verbose_name="ID Cliente",null=False,on_delete=models.CASCADE)
    Caracter = models.CharField(verbose_name="Caracter",max_length=50)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['No_Mat','Fecha_in','Id_C'],name='Id del Arribo')]
    
    def __str__(self):
        texto = "{0}"
        return texto.format(self.id)
    def __iter__(self):
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Vuelo": 
                value1=getattr(self,field_name.attname,None)
                vuelo = Vuelo.objects.get(id=value1)
                continue
            value=getattr(self,field_name.attname,None)
            if field_name.verbose_name == "No. Matricula": 
                self.No_Mat = str(vuelo.No_Mat)
                self.save()
                value = self.No_Mat
            if field_name.verbose_name == "Fecha de Entrada": 
                self.Fecha_in = vuelo.Fecha_in
                self.save()
                value = self.Fecha_in
            yield value
    def campos(self):
        output=[]
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Vuelo": continue
            output.append(field_name.verbose_name)
        return output