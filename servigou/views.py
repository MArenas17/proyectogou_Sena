from django.shortcuts import render,redirect
from .forms import *
from.models import *
#region de Publicacion
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

def actualizarP(request, id):
    publicacion = Publicacion.objects.get(id = id)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance = publicacion)
        if form.is_valid:
            form.save()
        return redirect('verP')
    else:
        form = PublicacionForm(instance = publicacion)
    context = {
        'form':form,
        'id': id}
    return render(request,'Publicación/CrearP.html',context)

def eliminarP(request,id):
    publicacion = Publicacion.objects.get(id = id)
    publicacion.delete()
    return redirect('verP')

#endregion
#region de Ruta
def crearR(request):
    if request.method == 'POST':
        form = RutaForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('crearR')
        else:
            return redirect('crearR')
    else:
        form = RutaForm()
    return render (request, 'Ruta/crearR.html',{'form':form})

def verR(request):
    ruta = Ruta.objects.all()
    return render(request,'Ruta/verR.html',{'ruta':ruta})

def actualizarR(request, id):
    ruta = Ruta.objects.get(id = id)
    if request.method == 'POST':
        form = RutaForm(request.POST, instance = ruta)
        if form.is_valid:
            form.save()
        return redirect('verR')
    else:
        form = RutaForm(instance = ruta)
    context = {
        'form':form,
        'id': id}
    return render(request,'Ruta/crearR.html',context)

def eliminarR(request,id):
    ruta = Ruta.objects.get(id = id)
    ruta.delete()
    return redirect('verR')
    
#endregion
#region de Usuario
def crearU(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('crearU')
        else:
            return redirect('crearU')
    else:
        form = UserForm()
    return render (request, 'Usuario/crearU.html',{'form':form})

def verU(request):
    usuario = User.objects.all()
    return render(request,'Usuario/verU.html',{'usuario':usuario})

def actualizarU(request, id):
    usuario = User.objects.get(id = id)
    if request.method == 'POST':
        form = UserForm(request.POST, instance = usuario)
        if form.is_valid:
            form.save()
        return redirect('verU')
    else:
        form = UserForm(instance = usuario)
    context = {
        'form':form,
        'id': id}
    return render(request,'Usuario/crearU.html',context)

def eliminarU(request,id):
    usuario = User.objects.get(id = id)
    usuario.delete()
    return redirect('verU')

#endregion



# def crearS(request):
#     if request.method == 'POST':
#         form = ServicioForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('crearS')
#         else:
#             return redirect('crearS')
#     else:
#         form = ServicioForm()
#     return render (request, 'Servicio/CrearS.html',{'form':form})