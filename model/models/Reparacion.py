from django.db import models
from .Servicio import Servicio


class Reparacion(models.Model):
    # El id de esta tabla se oculta, ya hay llave primaria
    # La Referencia a Servicio se oculta ya hay referencia por llave compuesta
    Id_S = models.ForeignKey(Servicio, verbose_name="ID Servicio", null=False, on_delete=models.CASCADE)
    Id_I = models.IntegerField(verbose_name="ID Instalacion", null=False)
    Codigo = models.IntegerField(verbose_name="Codigo", null=False)
    Tipo = models.CharField(verbose_name="Tipo", null=False, max_length=40)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['Id_I', 'Codigo', 'Tipo'], name='Id de Reparacion')]

    def __str__(self):
        texto = "{0}"
        return texto.format(self.id)

    def __iter__(self):
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Servicio":
                value1 = getattr(self, field_name.attname, None)
                servicio = Servicio.objects.get(id=value1)
                continue
            value = getattr(self, field_name.attname, None)
            if field_name.verbose_name == "ID Instalacion":
                self.Id_I = str(servicio.Id_I)
                self.save()
                value = self.Id_I
            if field_name.verbose_name == "Codigo":
                self.Codigo = servicio.Codigo
                self.save()
                value = self.Codigo
            yield value

    def campos(self):
        output = []
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Servicio": continue
            output.append(field_name.verbose_name)
        return output
