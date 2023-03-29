
from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name= 'index'),
    

    #HOME
    path('home_cliente/', views.home_cliente, name= 'home_cliente'),
    path('pendiente/', views.pendiente, name= 'pendiente'),
    path('home/', views.inicio, name= 'home'),

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
    path('pendiente/', views.pendiente, name="pendiente"),
    path('pendiente/<int:id>', views.pendiente, name="pendiente"),
    path('asignado/', views.asignado, name="asignado"),
    path('cancelarservicioasignado/<int:id>', views.cancelarservicioasignado, name="cancelarservicioasignado"),
    path('eliminarserviciocancelado/<int:id>', views.eliminarserviciocancelado, name="eliminarserviciocancelado"),
    path('eliminarpqrsf/<int:id>', views.eliminarpqrsf, name="eliminarpqrsf"),
    path('cancelado/', views.cancelado, name="cancelado"),
    path('enproceso/<int:id>', views.enproceso, name="enproceso"),
    path('enProceso/', views.enProceso, name="enProceso"),
    path('realizado/', views.realizado, name="realizado"),
    path('actualizarS/<int:id>', views.actualizarS, name='actualizarS'),
    path('eliminarS/<int:id>', views.eliminarS, name='eliminarS'),
    path('cancelar/servicio/<int:id>', views.cancelarServicio, name='cancelarS'),
    path('pendiente_cliente/', views.pendiente_cliente, name='pendiente_cliente'),

    #URL DE ROL
    path('crearRol/', views.crearRol, name="crearRol"),
    path('verRol/', views.verRol, name="verRol"),
    path('actualizarRol/<int:id>', views.actualizarRol, name='actualizarRol'),
    path('eliminarRol/<int:id>', views.eliminarRol, name='eliminarRol'),

    path('verpqrs/', views.verpqrs, name="verpqrs"),

    #Home_domici
    path('Home_repartidor/', views.Home_repartidor, name= 'Home_repartidor'),
    path('pendiente_rep/', views.pendiente_rep, name= 'pendiente_rep'),
    path('ServicioRealizado/<int:id>', views.ServicioRealizado, name="ServicioRealizado"),
    #end_domi

    path('asignacion/<int:id>', views.asignacion, name='asignacion'),
    path('reasignacion/<int:id>', views.reasignacion, name='reasignacion')
]
