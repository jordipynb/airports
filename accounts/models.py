from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model



class UserManager(BaseUserManager):
    def create_user(self, email, password, role, id_role):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user = self.model(
            email=self.normalize_email(email),
            role=role,
            id_role=id_role,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password, role="AG", id_role=0)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
        null=False,
        blank=False,
    )
    ROLE = (
        ("US", "Usuario Comun"),
        ("AI", "Administrador Instalaciones"),
        ("AA", "Administrador Aeropuertos"),
        ("AG", "Administrador General"),
    )
    role = models.CharField(max_length=2, choices=ROLE, default="US", null=False)
    id_role = models.IntegerField(null=False, default=0,verbose_name="email address")
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    def can_see(self, data):
        if self.role == 'AI':
            if data == "Servicio" or data == "Reparacion" or data == "Valoracion" or data == "ReparaNave" or data == "ReparacionesDependientes":
                return True
        elif self.role == 'AA':
            if data == 'Cliente' or data == "Nave" or data == "Vuelo" or data == "Arribo" or data == "Instalacion" or data == "Admin_de_Instalacion":
                return True
        return False
    def can_edit(self, data):
        if self.role == 'AI':
            if data == "Servicio" or data == "Reparacion" or data == "Valoracion" or data == "ReparaNave" or data == "ReparacionesDependientes":
                return True
        elif self.role == 'AA':
            if data == "Vuelo" or data == "Arribo" or data == "Instalacion" or data == "Admin_de_Instalacion":
                return True
        return False
    def can_delete(self, data):
        if self.role == 'AI':
            if data == "Servicio" or data == "Reparacion" or data == "Valoracion" or data == "ReparaNave" or data == "ReparacionesDependientes":
                return True
        elif self.role == 'AA':
            if data == "Vuelo" or data == "Arribo" or data == "Instalacion" or data == "Admin_de_Instalacion":
                return True
        return False
    def can_create(self, data):
        if self.role == 'AI':
            if data == "Servicio" or data == "Reparacion" or data == "Valoracion" or data == "ReparaNave" or data == "ReparacionesDependientes":
                return True
        elif self.role == 'AA':
            if data == "Vuelo" or data == "Arribo" or data == "Instalacion" or data == "Admin_de_Instalacion":
                return True
        return False

    class Meta:
        # User = get_user_model()
        app_label = 'accounts'

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_staff

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_staff

    def __iter__(self):
        for field_name in self._meta.fields:
            name=field_name.verbose_name
            if name == "email address" or name == "id":
                value=getattr(self,field_name.attname,None)
                yield value
            
    def campos(self):
        output=[]
        for field_name in self._meta.fields:
            name=field_name.verbose_name
            if name == "email address":
                output.append("Email address")
            elif name == "id":
                if self.role== "AA":
                    output.append("Aeropuerto")
        return output

    @property
    def is_staff(self):
        return self.role == "AG"

