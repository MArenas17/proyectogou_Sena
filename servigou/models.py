
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    documento = models.IntegerField(null=True, blank=False)
    celular = models.IntegerField(null=True, blank=False)
    direccion = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.first_name


class Ruta(models.Model):
    valor_km = models.BigIntegerField(null=False, blank=False)
    km = models.IntegerField(null=False, blank=False)
    porcentaje_liquidacion = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=2)
    incremento = models.IntegerField(null=True, blank=True)
    transporte = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=2)
    total_liquidacion = models.DecimalField(
        null=False, blank=False, max_digits=7, decimal_places=2)

    def __str__(self):
        return self.km

# De uno a muchos

# Servicio General

class Servicio(models.Model):
    fecha_hora = models.DateTimeField(default=timezone.now)
    tipo = models.CharField(max_length=30, null=False, blank=False)
    sector = models.CharField(max_length=30, null=False, blank=False)
    direccion = models.CharField(max_length=20, null=True, blank=False)
    celular = models.IntegerField(null=True, blank=False)
    descripcion = models.CharField(max_length=1000,null=False,blank=False)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

   
class ServicioRuta(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)

# De uno a muchos


class Publicacion(models.Model):
    nombre_publicacion = models.CharField(
        null=False, blank=False, max_length=20)
    tipo_archivo = models.CharField(null=False, blank=False, max_length=8)
    User = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre_publicacion


class Rol(models.Model):
    nombre_rol = models.CharField(null=False, blank=False, max_length=10)
    nivel_permiso = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre_rol


class UsuarioRol(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    rol = models.ForeignKey(Rol, on_delete=models.CASCADE)
    fecha_registro = models.DateField(null=False, blank=False)
