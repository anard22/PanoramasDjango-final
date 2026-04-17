from django import forms
from django.contrib.auth.models import User
from .models import Perfil


class UsuarioForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']


class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['rut', 'telefono', 'direccion']
            