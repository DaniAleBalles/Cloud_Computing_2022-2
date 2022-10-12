from proyecto.models import *
from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm 


class PasswordInput(forms.DateInput):
        input_type = 'password'

class label_pais (forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return  "%s" % obj.Pais

class Nameform(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','is_superuser')
        labels = {
            'is_superuser': 'Usted es administrador?',
        }

        

class FormUsuario(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ('Direccion', 'Documento', 'Tipo_Doc', 'Pais_id', 'Ciudad_id', 'Fecha_Expedicion', 'Celular')
        labels = {
            'Direccion': 'Direccion residencia',
            'Documento': 'Numero de documento',
            'Fecha_Expedicion': 'Fecha expedicion documento',
            'Celular': 'Numero de celular'
        }

class FormPaises(forms.ModelForm):

    class Meta:
        model = Paises
        fields =('Pais',)
        labels = {
            'Pais': 'Nombre del pais',
        }

class FormCiudades(forms.ModelForm):

    class Meta:
        model = Ciudades
        fields = ('Ciudad', 'id_pais')
        labels = {
            'Ciudad': 'Ciudad',
        }
    id_pais = label_pais(
        queryset=Paises.objects.all(),
        label='Pais donde esta ubicada la ciudad'
    )

class FormMonedas(forms.ModelForm):

    class Meta:
        model = Monedas
        fields = ('Moneda', 'Codigo', 'Valor_USD')
        labels = {
            'Moneda': 'Moneda',
            'Codigo': 'Codigo moneda',
            'Valor_USD': 'Valor en dólares'
        }

class FormTarifas(forms.ModelForm):

    class Meta:
        model = Tarifas
        fields = ('Tarifa',)
        labels = {
            'Tarifa': 'Tarifa de traansacción'
        }

class FormDestinatarios(forms.ModelForm):

    class Meta:
        model = Destinatario
        fields = ('Destinatario', 'Usuario_Dest')
        labels = {
            'Destinatario': 'Nombre de Contacto',
            'Usuario_Dest': 'Usuario del destinatario'
        }

class FormTransacciones(forms.ModelForm):

    class Meta:
        model = Transacciones
        fields = ('Envio',)
        labels = {
            'Envio': 'Cantidad  enviar'
        }
