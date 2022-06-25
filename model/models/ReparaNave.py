from django.db import models
from .Reparacion import Reparacion
from .Vuelo import Vuelo
class ReparaNave(models.Model):
    # El id de esta tabla se oculta, ya hay llave primaria
    # La Referencia a Reparacion se oculta ya hay referencia por llave compuesta
    # La Referencia a Vuelo se oculta ya hay referencia por llave compuesta
    Id_Rep = models.ForeignKey(Reparacion,verbose_name="ID Reparacion",null=False,on_delete=models.CASCADE)
    Id_V = models.ForeignKey(Vuelo,verbose_name="ID Vuelo",null=False,on_delete=models.CASCADE)
    Id_I = models.IntegerField(verbose_name="ID Instalacion",null=False)
    Codigo = models.IntegerField(verbose_name="Codigo",null=False)
    Tipo = models.CharField(verbose_name="Tipo",null=False,max_length=40)
    No_Mat = models.CharField(verbose_name="No. Matricula",null=False,max_length=30)
    Fecha_in = models.DateTimeField(verbose_name="Fecha de Entrada",null=False)
    Fecha_Ini = models.DateTimeField(verbose_name="Fecha Inicial",null=False)
    Tiempo_P = models.DateTimeField(verbose_name="Tiempo Planificado",null=False)
    Fecha_Fin = models.DateTimeField(verbose_name="Fecha Final",null=False)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['Id_I','Codigo','Tipo','No_Mat','Fecha_in','Fecha_Ini'],name='Id de Repara Nave')]

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id)
    def __iter__(self):
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Reparacion":
                value1=getattr(self,field_name.attname,None)
                reparacion = Reparacion.objects.get(id=value1)
                continue
            if field_name.verbose_name == "ID Vuelo": 
                value2=getattr(self,field_name.attname,None)
                vuelo = Vuelo.objects.get(id=value2)
                continue
            value=getattr(self,field_name.attname,None)
            if field_name.verbose_name == "ID Instalacion": 
                self.Id_I = reparacion.Id_I
                self.save()
                value = self.Id_I
            if field_name.verbose_name == "Codigo": 
                self.Codigo = reparacion.Codigo
                self.save()
                value = self.Codigo
            if field_name.verbose_name == "Tipo": 
                self.Tipo = reparacion.Tipo
                self.save()
                value = self.Tipo
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
            if field_name.verbose_name == "ID Reparacion": continue
            if field_name.verbose_name == "ID Vuelo": continue
            output.append(field_name.verbose_name)
        return output  