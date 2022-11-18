from django.contrib import admin
from .models import User,Publicacion,Ruta,Servicio
# Register your models here.
admin.site.register(User)
admin.site.register(Ruta)
admin.site.register(Publicacion)
admin.site.register(Servicio)
