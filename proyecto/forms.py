from proyecto.models import *
from django import forms 
from django.contrib.auth.models import User 


class Nameform(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'password', 'first_name', 'last_ name', 'email', 'password')
        labels = {
            'username': 'Nombre de usuario',
            'password': 'Contraseña',
            'first_name': 'Primer nombre',
            'last_name': 'Apellido',
            'email': 'Correo',
            'password': 'Contraseña'
        }

class Usuario(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('Direccion', 'Documento', 'Fecha_Expedicion', 'Celular')
        labels = {
            'Direccion': 'Direccion residencia',
            'Documento': 'Numero de documento',
            'Fecha_Expedicion': 'Fecha expedicion documento',
            'Celular': 'Numero de celular'
        }

class Paises(forms.ModelForm):

    class Meta:
        model = Paises
        fields =('Pais')
        labels = {
            'Pais': 'Pais de residencia',
        }

class Ciudades(forms.ModelForm):

    class Meta:
        model = Ciudades
        fields = ('Ciudad')
        labels = {
            'Ciudad': 'Ciudad'
        }

class Tipo_Documento(forms.ModelForm):

    class Meta:
        model = Tipo_Doc
        fields = ('Tipo_Doc')
        labels = {
            'Tipo_Doc': 'Tipo de documento',
        }

class Monedas(forms.ModelForm):

    class Meta:
        model = Monedas
        fields = ('Moneda', 'Código', 'Valor_USD')
        labels = {
            'Moneda': 'Moneda',
            'Código': 'Código moneda',
            'Valor_USD': 'Valor en dólares'
        }

class Tarifas(forms.ModelForm):

    class Meta:
        model = Tarifas
        fields = ('Tarifa')
        labels = {
            'Tarifa': 'Tarifa de traansacción'
        }

class Destinatarios(forms.ModelForm):

    class Meta:
        model = Destinatario
        fields = ('Destinatario')
        labels = {
            'Destinatario': 'Nombre de Contacto'
        }

class Transacciones(forms.ModelForm):

    class Meta:
        model = Transacciones
        fields = ('Envio')
        labels = {
            'Envio': 'Cantidad  enviar'
        }
