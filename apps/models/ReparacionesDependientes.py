from django.db import models
from.Reparacion import Reparacion
class ReparacionesDependientes(models.Model):
    # El id de esta tabla se oculta, ya hay llave primaria
    # La Referencia a Reparacion se oculta ya hay referencia por llave compuesta
    # La Referencia a Reparacion se oculta ya hay referencia por llave compuesta
    Id_Rep = models.ForeignKey(Reparacion,verbose_name="ID Reparacion",null=False,related_name="reparacion",on_delete=models.CASCADE)
    Id_RepDep = models.ForeignKey(Reparacion,verbose_name="ID Reparacion Dep",null=False,related_name="dependiente",on_delete=models.CASCADE)
    Id_I = models.IntegerField(verbose_name="ID Instalacion",null=False)
    Codigo = models.IntegerField(verbose_name="Codigo",null=False)
    Tipo = models.CharField(verbose_name="Tipo",null=False,max_length=40)
    Id_IDep = models.IntegerField(verbose_name="ID Instalacion Dep",null=False)
    Codigo_Dep = models.IntegerField(verbose_name="Codigo Dep",null=False)
    Tipo_Dep = models.CharField(verbose_name="Tipo Dep",null=False,max_length=40)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['Id_I','Codigo','Tipo','Id_IDep','Codigo_Dep','Tipo_Dep'],name='Id de Reparaciones Dep')]

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id)
    def __iter__(self):
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Reparacion":
                value1=getattr(self,field_name.attname,None)
                reparacion1 = Reparacion.objects.get(id=value1)
                continue
            if field_name.verbose_name == "ID Reparacion Dep": 
                value2=getattr(self,field_name.attname,None)
                reparacion2 = Reparacion.objects.get(id=value2)
                continue
            value=getattr(self,field_name.attname,None)
            if field_name.verbose_name == "ID Instalacion": 
                self.Id_I = reparacion1.Id_I
                self.save()
                value = self.Id_I
            if field_name.verbose_name == "Codigo": 
                self.Codigo = reparacion1.Codigo
                self.save()
                value = self.Codigo
            if field_name.verbose_name == "Tipo": 
                self.Tipo = reparacion1.Tipo
                self.save()
                value = self.Tipo
            if field_name.verbose_name == "ID Instalacion Dep": 
                self.Id_IDep = reparacion2.Id_I
                self.save()
                value = self.Id_IDep
            if field_name.verbose_name == "Codigo Dep": 
                self.Codigo_Dep = reparacion2.Codigo
                self.save()
                value = self.Codigo_Dep
            if field_name.verbose_name == "Tipo Dep": 
                self.Tipo_Dep = reparacion2.Tipo
                self.save()
                value = self.Tipo_Dep
            yield value
    def campos(self):
        output=[]
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Reparacion": continue
            if field_name.verbose_name == "ID Reparacion Dep": continue
            output.append(field_name.verbose_name)
        return output  