
from django.urls import path
from .import views
urlpatterns = [

    path('CrearPublicacion/', views.crearpublicacion, name='Crearpublicacion' ),
    path('verP/', views.verP, name='verP')
]