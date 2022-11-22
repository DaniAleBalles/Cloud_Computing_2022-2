from django.db import models
from django.contrib.auth.models import User
from . import dic
# Create your models here.

class Paises(models.Model):
    id_Pais = models.AutoField(primary_key=True, null=False, unique=True)
    Pais = models.CharField('Pais :', max_length=150, blank=False, null=False)

class Ciudades(models.Model):
    id_Ciudad = models.AutoField(primary_key=True, null=False, unique=True)
    Ciudad = models.CharField('Ciudad :', max_length=150, blank=False, null=False)
    id_pais = models.ForeignKey(Paises, max_length=150, blank=False, null=True, on_delete=models.SET_NULL, db_constraint=True)

class Monedas(models.Model):
    id_Moneda = models.AutoField(primary_key=True, null=False, unique=True)
    Moneda = models.CharField('Nombre de la moneda :', max_length=150, blank=False, null=False)
    Codigo = models.CharField('Código de la moneda :', max_length=6, blank=False, null=False)
    Valor_USD = models.FloatField('Valor en dólares :', null=False, blank=False)
    archivo=models.BooleanField('Archivo del registro'  , blank=True,null=False, default=0)


class Tarifas(models.Model):
    id_Tarifa = models.AutoField(primary_key=True, null=False, unique=True)
    Tarifa = models.IntegerField('Tarifa por transacción:', null=False, blank=False)

class Usuario(models.Model):
    id_Usuario = models.AutoField(primary_key=True, null=False, unique=True)
    User_id = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Pais_id = models.ForeignKey(Paises, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Ciudad_id = models.ForeignKey(Ciudades, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Direccion = models.CharField('Dirección de residencia :', max_length=150, null=True, blank=False)
    Documento = models.CharField('Documento :', max_length=150, null=True, blank=False)
    Tipo_Doc= models.IntegerField(choices=dic.Documento,blank=False, null=True, default=0)
    Fecha_Expedicion = models.DateField('Fecha de Expedicion :', null=True, blank=False)
    Celular = models.IntegerField('Número de celular :', null=True, blank=False)
    Monto = models.IntegerField('Monto en la cuenta :', default=0 ,null=True, blank=False)

class Destinatario(models.Model):
    id_Destinatario = models.AutoField(primary_key=True, null=False, unique=True)
    Usuario_Dest = models.ForeignKey(User, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Destinatario = models.CharField('Nombre del destinatario :', max_length=150, null=False, blank=False)

class Transacciones(models.Model):
    id_Transaccion = models.AutoField(primary_key=True, null=False, unique=True)    
    Usuario_dest = models.ForeignKey(Usuario, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Tasa_id = models.ForeignKey(Monedas, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Tarifa_id = models.ForeignKey(Tarifas, null=True, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Envio = models.IntegerField('Monto enviado :', null=False, blank=False)
    Destino = models.IntegerField('Monto Destino :', null=True, blank=True)
    Fecha = models.DateTimeField('Fecha y hora transacción :', null=True, blank=True)

