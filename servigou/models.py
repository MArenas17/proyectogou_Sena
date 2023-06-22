from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone


class User(AbstractUser):
    documento = models.IntegerField(unique=True, null=True, blank=False)
    celular = models.IntegerField(null=True, blank=False)
    direccion = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.first_name


class Ruta(models.Model):
    nombre = models.CharField(max_length=30, null=False, blank=False, default='ruta')
    valor = models.BigIntegerField(null=False, blank=False)
    descripcion = models.CharField(max_length=100, null=False, blank=False, default='ruta')

    def __str__(self):
        return self.nombre


# De uno a muchos

# Servicio General

class Servicio(models.Model):
    fecha_hora = models.DateTimeField(default=timezone.now)
    tipo = models.CharField(max_length=30, null=False, blank=False)
    direccion = models.CharField(max_length=20, null=True, blank=False)
    celular = models.CharField(max_length=13,null=True, blank=False)
    descripcion = models.CharField(max_length=1000, null=False, blank=False)
    estado = models.CharField(max_length=50, default='sin_asignar')
    repartidor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='repartidor', default=1, null=True)
    User = models.ForeignKey(User,on_delete=models.CASCADE, related_name='User')
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, related_name='ruta', default=1)

    def __str__(self):
        return self.descripcion


class ServicioRuta(models.Model):
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE)
    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)


class Pqrs(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    asunto = models.CharField(max_length=30, null=False, blank=False)
    mensaje = models.TextField(max_length=500, null=False, blank=False)


# De uno a muchos


class Publicacion(models.Model):
    nombre_publicacion = models.CharField(null=False, blank=False, max_length=20)
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

