from django.db import models
from django.contrib.auth.models import User 
# Create your models here.

class Paises(models.Model):
    id_Pais = models.AutoField(primary_key=True, null=False, unique=True)
    Pais = models.CharField('Pais :', max_length=150, blank=False, null=False)

class Ciudades(models.Model):
    id_Ciudad = models.AutoField(primary_key=True, null=False, unique=True)
    Ciudad = models.CharField('Ciudad :', max_length=150, blank=False, null=False)

class Tipo_Doc(models.Model):
    id_Tdoc = models.AutoField(primary_key=True, null=False, unique=True)
    Tipo_Doc= models.CharField('Tipo de documento :', max_length=150, blank=False, null=False)

class Monedas(models.Model):
    id_Moneda = models.AutoField(primary_key=True, null=False, unique=True)
    Moneda = models.CharField('Nombre de la moneda :', max_length=150, blank=False, null=False)
    Código = models.CharField('Código de la moneda :', max_length=6, blank=False, null=False)
    Valor_USD = models.IntegerField('Valor en dólares :', null=False, blank=False)

class Tarifas(models.Model):
    id_Tarifa = models.AutoField(primary_key=True, null=False, unique=True)
    Tarifa = models.IntegerField('Tarifa por transacción:', null=False, blank=False)

class Usuario(models.Model):
    id_Usuario = models.AutoField(primary_key=True, null=False, unique=True)
    User_id = models.ForeignKey(User, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Pais_id = models.ForeignKey(Paises, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Ciudad_id = models.ForeignKey(Ciudades, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Direccion = models.CharField('Dirección de residencia :', max_length=150, null=False, blank=False)
    Tipo_Doc_id = models.ForeignKey(Tipo_Doc, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Documento = models.CharField('Documento :', max_lenght=150, null=False, blank=False)
    Celular = models.IntegerField('Número de celular :', null=False, blank=False)
    Monto = models.IntegerField('Monto en la cuenta :', default=0 ,null=False, blank=False)

class Destinatario(models.Model):
    id_Destinatario = models.AutoField(primary_key=True, null=False, unique=True)
    Usuario_Dest = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Destinatario = models.CharField('Nombre del destinatario :', max_length=150, null=False, blank=False)

class Transacciones(models.Model):
    id_Transaccion = models.AutoField(primary_key=True, null=False, unique=True)    
    Usuario = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Usuario_Dest = models.ForeignKey(Usuario, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Tasa_id = models.ForeignKey(Monedas, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Tarifa_id = models.ForeignKey(Tarifas, null=False, blank=False, on_delete=models.SET_NULL, db_constraint=True)
    Envio = models.IntegerField('Monto enviado :', null=False, blank=False)
    Destino = models.IntegerField('Monto Destino :', null=False, blank=False)
    Fecha = models.DateTimeField('Fecha y hora transacción :', null=False, blank=False)

