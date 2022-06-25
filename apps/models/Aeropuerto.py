from django.db import models
class Aeropuerto(models.Model):
    Nom_A = models.CharField(verbose_name="Nombre",max_length=50,null=False,unique=True)
    Direccion = models.CharField(verbose_name="Direccion",max_length=100,null=False)
    Pos_Geo = models.CharField(verbose_name="Posicion Geografica",max_length=50,null=False)

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