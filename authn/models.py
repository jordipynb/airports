from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirma contraseña', widget=forms.PasswordInput)

    class Meta(UserCreationForm):
        model = User
        fields = ['email', 'password1', 'password2']