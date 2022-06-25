from django.db import models
class Cliente(models.Model):
    Nom_C = models.CharField(verbose_name="Nombre",max_length=50,null=False,unique=True)
    Nacionalidad = models.CharField(verbose_name="Nacionalidad",max_length=50)
    Tipo_C = models.CharField(verbose_name="Tipo",max_length=75,null=False)

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