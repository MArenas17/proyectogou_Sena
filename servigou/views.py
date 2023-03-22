from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.shortcuts import render, redirect
import tkinter as tk
from tkinter import messagebox

from .forms import *
from .models import *


def index(request):
    if request.method == 'POST':
        form = PqrsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
        else:
            return redirect('index')

    form = PqrsForm()
    return render(request, 'layout\partials\Pprincipal\inicio.html', {'form': form})


# region de Publicacion
@login_required(login_url='login')
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
    return render(request, 'Publicación/CrearP.html', {'form': form})


@login_required(login_url='login')
def verP(request):
    publicacion = Publicacion.objects.all()
    return render(request, 'Publicación/verP.html', {'publicacion': publicacion})


@login_required(login_url='login')
def actualizarP(request, id):
    publicacion = Publicacion.objects.get(id=id)
    if request.method == 'POST':
        form = PublicacionForm(request.POST, instance=publicacion)
        if form.is_valid:
            form.save()
        return redirect('verP')
    else:
        form = PublicacionForm(instance=publicacion)
    context = {
        'form': form,
        'id': id}
    return render(request, 'Publicación/CrearP.html', context)


@login_required(login_url='login')
def eliminarP(request, id):
    publicacion = Publicacion.objects.get(id=id)
    publicacion.delete()
    return redirect('verP')


# endregion
# region de Ruta
@login_required(login_url='login')
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
    return render(request, 'Ruta/crearR.html', {'form': form})


@login_required(login_url='login')
def verR(request):
    ruta = Ruta.objects.all()
    return render(request, 'Ruta/verR.html', {'ruta': ruta})


@login_required(login_url='login')
def actualizarR(request, id):
    ruta = Ruta.objects.get(id=id)
    if request.method == 'POST':
        form = RutaForm(request.POST, instance=ruta)
        if form.is_valid:
            form.save()
            return redirect('verR')
    else:
        form = RutaForm(instance=ruta)
    context = {
        'form': form,
        'id': id}
    return render(request, 'Ruta/crearR.html', context)


@login_required(login_url='login')
def eliminarR(request, id):
    ruta = Ruta.objects.get(id=id)
    ruta.delete()
    return redirect('verR')


# endregion
# region de Usuario
def crearU(request):
    if request.method == 'POST':
        user = User.objects.create(
            username=request.POST['username'], first_name=request.POST['first_name'],
            password=request.POST['password'], direccion=request.POST['direccion'], email=request.POST['email'],
            documento=request.POST['documento'], celular=request.POST['celular'])
        user.set_password(request.POST['password'])
        user.save()
        user.groups.add(request.POST['groups'])
        user.save()
        return redirect('login')
    form = UserForm()
    context = {
        'form': form}
    return render(request, 'Usuario/crearU.html', context)


@login_required(login_url='login')
def verU(request):
    usuario = User.objects.all()
    return render(request, 'Usuario/verU.html', {'usuario': usuario})


# @login_required(login_url='login')
# def actualizarU(request, id):
#     usuario = User.objects.get(id=id)
#     if request.method == 'POST':
#         form = UserForm(request.POST, instance=usuario)
#         if form.is_valid:
#             form.save()
#             user = User.objects.get(id=id)
#             user.set_password(request.POST['password'])
#             user.save()
#             return redirect('verU')
#     else:
#         form = UserForm(instance=usuario)
#     context = {
#         'form': form,
#         'id': id}
#     return render(request, 'Usuario/crearU.html', context)

@login_required(login_url="login")
def actualizarU(request, id):
    usuario = UserForm.objects.get(id=id)
    if request.method == "POST":
        form = UserForm(request.POST, instance=usuario)
        if form.is_valid():
            identification = form.cleaned_data["documento"]
            email = form.cleaned_data["email"]
            existing_client_identification = (
                User.objects.filter(documento=identification).exclude(id=id).exists()
            )
            existing_client_email = (
                User.objects.filter(email=email).exclude(id=id).exists()
            )
            if existing_client_identification:
                messages.error(request, "El documento ya existe")
                return render(request, "Usuario/crearU.html", {"form": form})
            elif existing_client_email:
                messages.error(request, "El email ya existe")
                return render(request, "Usuario/crearU.html", {"form": form})
            else:
                form.save()
                return redirect('verU')
    else:
        form = UserForm(instance=usuario)
    context = {"form": form}
    return render(request, "Usuario/crearU.html", context)


def eliminarU(request, id):
    usuario = User.objects.get(id=id)
    usuario.delete()
    return redirect('verU')


# endregion
# region de Servicio
@login_required(login_url='login')
def crearS(request):
    idUser = request.user.id
    if request.method == 'POST':
        form = ServicioForm(request.POST, initial={"User": idUser})
        if form.is_valid:
            form.save()
            return redirect('home_cliente')
        else:
            return redirect('home_cliente')
    else:
        form = ServicioForm(initial={"User": idUser})
    return render(request, 'layout\Diseño_cliente\crearS.html', {'form': form})


@login_required(login_url='login')
def pendiente(request):
    servicios = Servicio.objects.select_related('ruta').filter(estado='sin_asignar').values(
        'fecha_hora', 'tipo', 'sector', 'direccion', 'celular', 'descripcion', 'ruta__transporte')
    return render(request, 'layout\Diseño_admin\pendiente.html', {'servicios': servicios})


@login_required(login_url='login')
def asignado(request):
    servicios = Servicio.objects.select_related('ruta').filter(estado='asignado').values(
        'fecha_hora', 'tipo', 'sector', 'direccion', 'celular', 'descripcion', 'ruta__transporte')
    return render(request, 'layout\Diseño_admin\pendiente.html', {'servicios': servicios})


@login_required(login_url='login')
def cancelado(request):
    servicios = Servicio.objects.filter(estado='cancelado')
    return render(request, 'layout\Diseño_admin\cancelado.html', {'servicios': servicios})


@login_required(login_url='login')
def realizado(request):
    servicios = Servicio.objects.filter(estado='realizado')
    return render(request, 'layout\Diseño_admin\pendiente.html', {'servicios': servicios})


def cancelarServicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.estado = "cancelado"
    servicio.save()
    print(id)
    return redirect('pendiente')


@login_required(login_url='login')
def actualizarS(request, id):
    servicios = Servicio.objects.get(id=id)
    if request.method == 'POST':
        form = ServicioForm(request.POST, instance=servicios)
        if form.is_valid:
            form.save()
        return redirect('verS')
    else:
        form = ServicioForm(instance=servicios)
    context = {
        'form': form,
        'id': id}
    return render(request, 'Servicio/crearS.html', context)


@login_required(login_url='login')
def eliminarS(request, id):
    usuario = Servicio.objects.get(id=id)
    usuario.delete()
    return redirect(crearU)


# endregion

# region de Rol
@login_required(login_url='login')
def crearRol(request):
    if request.method == 'POST':
        form = RolForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('crearRol')
        else:
            return redirect('crearRol')
    else:
        form = RolForm()
    return render(request, 'Rol/crearRol.html', {'form': form})


@login_required(login_url='login')
def verRol(request):
    usuario = Rol.objects.all()
    return render(request, 'Rol/verRol.html', {'usuario': usuario})


@login_required(login_url='login')
def actualizarRol(request, id):
    rol = Rol.objects.get(id=id)
    if request.method == 'POST':
        form = RolForm(request.POST, instance=rol)
        if form.is_valid:
            form.save()
        return redirect('verRol')
    else:
        form = RolForm(instance=rol)
    context = {
        'form': form,
        'id': id}
    return render(request, 'Rol/crearRol.html', context)


@login_required(login_url='login')
def eliminarRol(request, id):
    rol = Rol.objects.get(id=id)
    rol.delete()
    return redirect('verRol')


# endregion

# region home
@login_required(login_url='login')
def inicio(request):
    if request.user.groups.filter(name='Cliente').exists():
        return redirect('home_cliente')
    elif request.user.groups.filter(name='Repartidor').exists():
        return redirect('Home_repartidor')
    return render(request, 'layout\Diseño_admin\home.html')


@login_required(login_url='login')
def home_cliente(request):
    return render(request, 'layout\Diseño_cliente\home_cliente.html')


@login_required(login_url='login')
def pendiente(request):
    servicios = Servicio.objects.filter(estado='sin_asignar')
    context = {'servicios': servicios}
    return render(request, 'layout\Diseño_admin/pendiente.html', context)


def verpqrs(request):
    pqrs = Pqrs.objects.all()
    return render(request, 'layout/Diseño_admin/verpqrs.html', {'pqrs': pqrs})
# endregion

#repartidor
@login_required(login_url='login')
def Home_repartidor(request):
    return render(request, 'layout\Diseño_repartidor\Home_repartidor.html')
#endrepartidor
