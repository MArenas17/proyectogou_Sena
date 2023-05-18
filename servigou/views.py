from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.db import IntegrityError
from .forms import *
from .models import *
from django.http import HttpResponse
from django.conf import settings
from django.core.paginator import Paginator
import os
from django.db.models import Sum



def pdf(request, pdf_name):
    file_path = os.path.join(settings.MEDIA_ROOT, pdf_name)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response
    return HttpResponse("archivo no existe")


def index(request):
    if request.method == 'POST':
        form = PqrsForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('index')
        else:
            return redirect('index')

    form = PqrsForm()
    return render(request, 'layout/partials/Pprincipal/inicio.html', {'form': form})


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
        form = UserForm(request.POST)
        try:
            user = User.objects.create(
                username=request.POST['username'], first_name=request.POST['first_name'],
                password=request.POST['password'], direccion=request.POST['direccion'], email=request.POST['email'],
                documento=request.POST['documento'], celular=request.POST['celular'])
            user.set_password(request.POST['password'])
            user.save()
            user.groups.add(request.POST['groups'])
            user.save()
            messages.success(request, 'Registro Exitoso!')
        except IntegrityError as e:
            error_message = str(e).replace('UNIQUE constraint failed: servigou_user.', '')
            messages.error(request, f"El campo '{error_message}' ya existe en la base de datos.")
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
    usuario = User.objects.get(id=id)
    if request.method == "POST":
        formUpdate = UserForm2(request.POST, instance=usuario)
        try:
            formUpdate.save()
            messages.success(request, "Actualizado correctamente")
        except Exception as e:
            messages.error(request, f"El error es : '{e}'")

    form = UserForm2(instance=usuario)
    context = {"form": form}
    return render(request, "Usuario/actualizarU.html", context)


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
        form = ServicioForm(request.POST,
                            initial={"User": idUser,
                                     "direccion": request.user.direccion,
                                     "celular": request.user.celular})
        if form.is_valid:
            form.save()
            return redirect('homecliente')
        else:
            return redirect('homecliente')
    else:
        form = ServicioForm(initial={"User": idUser})
    return render(request, 'layout/Disenocliente/crearS.html', {'form': form})


@login_required(login_url='login')
def asignado(request):
    servicios = Servicio.objects.filter(estado='asignado')
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    return render(request, 'layout/Disenoadmin/asignados.html', {'page_obj': servicios})


@login_required(login_url='login')
def cancelado(request):
    servicios = Servicio.objects.filter(estado='cancelado')
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    return render(request, 'layout/Disenoadmin/cancelado.html', {'page_obj': servicios})


@login_required(login_url='login')
def enProceso(request):
    servicios = Servicio.objects.filter(estado="enproceso")
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    return render(request, 'layout/Disenorepartidor/enproceso.html', {'page_obj': servicios})


@login_required(login_url='login')
def enprocesoA(request):
    servicios = Servicio.objects.filter(estado='enproceso')
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    return render(request, 'layout/Disenoadmin/enprocesoA.html', {'page_obj': servicios})

@login_required(login_url='login')
def enprocesocliente(request):
    cliente = request.user.id
    print(cliente)
    servicios = Servicio.objects.filter(estado='enproceso', User_id=cliente)
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    return render(request, 'layout/Disenocliente/enprocesocliente.html', {'page_obj': servicios})


@login_required(login_url='login')
def realizado(request):
    repartidor = request.user.id
    print(repartidor)
    servicios = Servicio.objects.filter(estado='realizado', Repartidor_id=repartidor)
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    return render(request, 'layout/Disenorepartidor/Realizado.html', {'page_obj': servicios})


@login_required(login_url='login')
def cancelarServicio(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.estado = "cancelado"
    servicio.save()
    print(id)
    return redirect('pendiente')


@login_required(login_url='login')
def cancelarservicioasignado(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.estado = "cancelado"
    servicio.save()
    print(id)
    return redirect('asignado')


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
    return redirect(pendientecliente)


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
        return redirect('homecliente')
    elif request.user.groups.filter(name='Repartidor').exists():
        return redirect('Homerepartidor')
    return render(request, 'layout/Disenoadmin/home.html', {})


@login_required(login_url='login')
def homecliente(request):
    return render(request, 'layout/Disenocliente/homecliente.html')


@login_required(login_url='login')
def pendiente(request):
    servicios = Servicio.objects.filter(estado='sin_asignar')
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    context = {'page_obj': servicios}
    return render(request, 'layout/Disenoadmin/pendiente.html', context)


def verpqrs(request):
    pqrs = Pqrs.objects.all()
    paginator = Paginator(pqrs, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    pqrs = paginator.get_page(page)  # Obtener los elementos para la página actual
    return render(request, 'layout/Disenoadmin/verpqrs.html', {'page_obj': pqrs})


@login_required(login_url='login')
def serviciosrealizados(request):
    fecha_inicial = request.GET.get('fecha_inicial')
    fecha_final = request.GET.get('fecha_final')
    repartidor = request.GET.get('repartidor')

    servicios = Servicio.objects.filter(estado='realizado')

    if fecha_inicial:
        servicios = servicios.filter(fecha_hora__gte=fecha_inicial)

    if fecha_final:
        servicios = servicios.filter(fecha_hora__lte=fecha_final)

    if repartidor:
        servicios = Servicio.objects.filter(Repartidor__icontains=repartidor)

    total_valor = servicios.aggregate(total=Sum('ruta__valor'))['total']
    valor_25_porcentaje = total_valor * 0.25


    paginator = Paginator(servicios, 10)  # Mostrar 10 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual

    context = {
    'page_obj': servicios,
    'fecha_inicial': fecha_inicial,
    'fecha_final': fecha_final,
    'repartidor': repartidor,
    'total_valor': total_valor,
    'valor_25_porcentaje': valor_25_porcentaje
}


    return render(request, 'layout/Disenoadmin/Realizado.html', context)




# endregion

# region repartidor
@login_required(login_url='login')
def Homerepartidor(request):
    return render(request, 'layout/Disenorepartidor/Homerepartidor.html')


@login_required(login_url='login')
def pendienterep(request):
    repartidor = request.user.id
    print(repartidor)
    servicios = Servicio.objects.filter(estado='asignado', Repartidor_id=repartidor)
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    return render(request, 'layout/Disenorepartidor/pendienterep.html', {'page_obj': servicios})


@login_required(login_url='login')
def pendientecliente(request):
    servicios = Servicio.objects.filter(estado='sin_asignar', User=request.user)
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    context = {'page_obj': servicios}
    return render(request, 'layout/Disenocliente/pendientecliente.html', context)



@login_required(login_url='login')
def pendiente(request):
    servicios = Servicio.objects.filter(estado='sin_asignar')
    paginator = Paginator(servicios, 10)  # Mostrar 7 elementos por página
    page = request.GET.get('page')  # Obtener el número de página actual desde la solicitud GET
    servicios = paginator.get_page(page)  # Obtener los elementos para la página actual
    context = {'page_obj': servicios}
    return render(request, 'layout/Disenoadmin/pendiente.html', context)



@login_required(login_url='login')
def asignacion(request, id):
    form = AsignacionForm()
    servicio = Servicio.objects.get(id=id)
    if request.method == 'POST':
        repartidor = User.objects.get(id=request.POST['Repartidor'])
        servicio.Repartidor = repartidor
        servicio.estado = 'asignado'
        servicio.save()
        return redirect('pendiente')
    context = {'form': form}
    return render(request, 'layout/Disenoadmin/asignacion.html', context)


@login_required(login_url='login')
def reasignacion(request, id):
    form = AsignacionForm()
    servicio = Servicio.objects.get(id=id)
    if request.method == 'POST':
        repartidor = User.objects.get(id=request.POST['Repartidor'])
        servicio.Repartidor = repartidor
        servicio.estado = 'asignado'
        servicio.save()
        return redirect('asignado')
    context = {'form': form}
    return render(request, 'layout/Disenoadmin/asignacion.html', context)


@login_required(login_url='login')
def ServicioRealizado(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.estado = 'realizado'
    servicio.save()
    print(id)
    return redirect('enProceso')


@login_required(login_url='login')
def enproceso(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.estado = "enproceso"
    servicio.save()
    print(id)
    return redirect('pendienterep')

@login_required(login_url='login')
def enprocesoCliente(request, id):
    servicio = Servicio.objects.get(id=id)
    servicio.estado = "enprocesocliente"
    servicio.save()
    print(id)
    return redirect('enprocesocliente')


@login_required(login_url='login')
def eliminarserviciocancelado(request, id):
    usuario = Servicio.objects.get(id=id)
    usuario.delete()
    return redirect('cancelado')


@login_required(login_url='login')
def eliminarpqrsf(request, id):
    usuario = Pqrs.objects.get(id=id)
    usuario.delete()
    return redirect('verpqrs')

@login_required(login_url='login')
def consolidado(request):
    form = consolidado
    context = {'form': form}
    return render(request, 'layout/Disenoadmin/consolidado.html', context)

# endregion
