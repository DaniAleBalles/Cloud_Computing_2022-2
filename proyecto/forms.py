from django import forms 
from django.contrib.auth.models import User 

class Nameform(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name')
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contraseña',
            'first_name': 'puta 343',
        }
    