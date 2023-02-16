
from django.urls import path
from .import views
urlpatterns = [
    path('', views.index, name= 'index'),
    #URL DE PUBLICACION
    path('CrearPublicacion/', views.crearpublicacion, name='Crearpublicacion' ),
    path('verP/', views.verP, name='verP'),
    path('actualizarP/<int:id>', views.actualizarP, name='actualizarP'),
    path('eliminarP/<int:id>', views.eliminarP, name='eliminarP'),

     #URL DE RUTA
    path('crearR/', views.crearR, name='crearR' ),
    path('verR/', views.verR, name='verR'),
    path('actualizarR/<int:id>', views.actualizarR, name='actualizarR'),
    path('eliminarR/<int:id>', views.eliminarR, name='eliminarR'),

     #URL DE USUARIO
    path('crearU/', views.crearU, name='crearU' ),
    path('verU/', views.verU, name='verU'),
    path('actualizarU/<int:id>', views.actualizarU, name='actualizarU'),
    path('eliminarU/<int:id>', views.eliminarU, name='eliminarU'),
    
     #URL DE SERVICIO
    path('crearS/', views.crearS, name="crearS"),
    path('verS/', views.verS, name="verS"),
    path('actualizarS/<int:id>', views.actualizarS, name='actualizarS'),
    path('eliminarS/<int:id>', views.eliminarS, name='eliminarS'),

    #URL DE ROL
    path('crearRol/', views.crearRol, name="crearRol"),
    path('verRol/', views.verRol, name="verRol"),
    path('actualizarRol/<int:id>', views.actualizarRol, name='actualizarRol'),
    path('eliminarRol/<int:id>', views.eliminarRol, name='eliminarRol'),

    #URL DE INICIO
    path('inicio/',views.inicio, name="inicio")
]
    