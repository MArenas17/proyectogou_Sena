
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    documento = models.IntegerField(null=True, blank=False)
    celular = models.IntegerField(null=True, blank=False)
    direccion = models.CharField(max_length=20, null=True, blank=False)

    def __str__(self):
        return self.first_name


class Ruta(models.Model):
    valor_km = models.BigIntegerField(null=False,blank=False)
    km = models.IntegerField(null=False,blank=False)
    porcentaje_liquidacion = models.DecimalField(null=False,blank=False,max_digits=7,decimal_places=2)
    incremento = models.IntegerField(null=True, blank=True)
    total_servicio = models.DecimalField(null=False,blank=False,max_digits=7,decimal_places=2)
    total_liquidacion = models.DecimalField(null=False,blank=False,max_digits=7,decimal_places=2)
    
    def __str__(self):
        return self.km
#De uno a muchos
class Servicio(models.Model):
    fecha_hora = models.DateTimeField(null=False,blank=False)
    estado_servicio = models.CharField( max_length=10,null=False,blank=False)
    producto = models.CharField(max_length=200)
    User = models.ForeignKey(User, on_delete=models.PROTECT)
    ruta = models.ForeignKey(Ruta, on_delete=models.PROTECT )
    
    def __str__(self):
        return self.documento

#De uno a muchos
class Publicacion(models.Model):
    nombre_publicacion = models.CharField(null=False, blank=False, max_length=20 )
    tipo_archivo = models.CharField(null=False, blank=False, max_length=8)
    User = models.ForeignKey(User, on_delete=models.PROTECT )

    def __str__(self):
        return self.nombre_publicacion
#De muchos a muchos