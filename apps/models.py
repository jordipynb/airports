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

class Nave(models.Model):
    No_Mat = models.CharField(verbose_name="No. Matricula",null=False,unique=True,max_length=30)
    Clasific = models.CharField(verbose_name="Clasificacion",null=False,max_length=50)
    Capacidad = models.SmallIntegerField(verbose_name="Capacidad",null=False)
    No_Trip = models.SmallIntegerField(verbose_name="No. Tripulantes",null=False)
    # Este ID queda oculto
    Id_Plazas = models.ForeignKey(Plazas,verbose_name='ID Plazas',on_delete=models.CASCADE)
    Id_D = models.ForeignKey(Cliente, verbose_name="ID Dueño",null=False,on_delete=models.CASCADE)

    def __str__(self):
        texto = "{0}"
        return texto.format(self.No_Mat)
    def __iter__(self):
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Plazas": continue
            value=getattr(self,field_name.attname,None)
            yield value
    def campos(self):
        output=[]
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Plazas": continue
            output.append(field_name.verbose_name)
        return output

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

class Instalacion(models.Model):
    Nom_I = models.CharField(verbose_name="Nombre",null=False,max_length=40)
    Tipo_I = models.CharField(verbose_name="Tipo",null=False,max_length=50)
    Ubicacion = models.CharField(verbose_name="Ubicacion",max_length=50)
    Id_A = models.ForeignKey(Aeropuerto,verbose_name="ID Aeropuerto",on_delete=models.CASCADE)

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

class Reparacion(models.Model):
    # El id de esta tabla se oculta, ya hay llave primaria
    # La Referencia a Servicio se oculta ya hay referencia por llave compuesta
    Id_S = models.ForeignKey(Servicio,verbose_name="ID Servicio",null=False,on_delete=models.CASCADE)
    Id_I = models.IntegerField(verbose_name="ID Instalacion",null=False)
    Codigo = models.IntegerField(verbose_name="Codigo",null=False)
    Tipo = models.CharField(verbose_name="Tipo",null=False,max_length=40)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['Id_I','Codigo','Tipo'],name='Id de Reparacion')]

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
            value=getattr(self,field_name.attname,None)
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
        output=[]
        for field_name in self._meta.fields:
            if field_name.verbose_name == "ID": continue
            if field_name.verbose_name == "ID Servicio": continue
            output.append(field_name.verbose_name)
        return output  

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