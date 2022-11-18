from django.shortcuts import render,redirect
from .forms import PublicacionForm
from.models import *

def crearpublicacion(request):
    if request.method == 'POST':
        form = PublicacionForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('Crearpublicacion')
        else:
            return redirect('Crearpublicacion')
    else:
        form = PublicacionForm()
    return render (request, 'Publicación/CrearP.html',{'form':form})

def verP(request):
    publicacion = Publicacion.objects.all()
    return render(request,'Publicación/verP.html',{'publicacion':publicacion})
