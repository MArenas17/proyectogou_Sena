
from django.urls import path
from .import views
urlpatterns = [

    path('CrearPublicacion/', views.crearpublicacion, name='Crearpublicacion' ),
    path('verP/', views.verP, name='verP'),
    path('actualizarP/<int:id>', views.actualizarP, name='actualizarP'),
    path('eliminarP/<int:id>', views.eliminarP, name='eliminarP'),
    
    path('crearR/', views.crearR, name='crearR' ),
    path('verR/', views.verR, name='verR'),
    path('actualizarR/<int:id>', views.actualizarR, name='actualizarR'),
    path('eliminarR/<int:id>', views.eliminarR, name='eliminarR'),

    path('crearU/', views.crearU, name='crearU' ),
    path('verU/', views.verU, name='verU'),
    path('actualizarU/<int:id>', views.actualizarU, name='actualizarU'),
    path('eliminarU/<int:id>', views.eliminarU, name='eliminarU'),


    # path('crearS/', views.crearS, name="crearS"),
]
    