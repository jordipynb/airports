from django.db import models
class Plazas(models.Model):
    # El id de esta tabla se oculta, ya hay llave primaria
    Clasific = models.CharField(verbose_name="Clasificacion",null=False,max_length=40)
    No_Trip = models.SmallIntegerField(verbose_name="No. Tripulantes",null=False)
    Capacidad = models.SmallIntegerField(verbose_name="Capacidad",null=False)
    Total_P = models.SmallIntegerField(verbose_name="Total de Plazas")
    class Meta:
        constraints = [models.UniqueConstraint(fields=['Clasific','No_Trip','Capacidad'],name='Id de Plazas')]

    def __str__(self):
        texto = "{0} {1} {2}"
        return texto.format(self.Clasific, self.No_Trip, self.Capacidad)
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