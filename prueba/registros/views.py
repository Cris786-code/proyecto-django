from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm
from .models import Archivos
from .forms import FormArchivos
from django.contrib import messages


def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tu mensaje ha sido enviado correctamente.')
            return redirect('contacto')
    
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {'form': form})


def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})



def contacto(request):
    return render(request, "registros/contacto.html")


def consultarComentarioIndividual(request, id):
    comentario=ComentarioContacto.objects.get(id=id)
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})


def editarComentarioContacto(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    form = ComentarioContactoForm(request.POST, instance=comentario)
    if form.is_valid():
        form.save() #si el registro ya existe, se modifica.
        comentarios=ComentarioContacto.objects.all()
        return render(request,"registros/consultarComentario.html",
        {'comentarios':comentarios})
    return render(request,"registros/formEditarComentario.html",
    {'comentario':comentario})


def eliminarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, id=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})
    return render(request, 'registros/confirmarEliminarComentario.html', {'comentario': comentario})


def archivos(request):
    if request.method == 'POST':
        form = FormArchivos(request.POST, request.FILES)
        if form.is_valid():
            titulo = request.POST['titulo']
            descripcion = request.POST['descripcion']
            archivo = request.FILES['archivo']
            insert = Archivos(titulo=titulo, descripcion=descripcion, archivo=archivo)
            insert.save()
            return render(request, "registros/archivos.html")
        else:
            messages.error(request, 'Error al procesar el formulario. Por favor, verifica los datos ingresados.')
    else:
        return render(request, "registros/archivos.html", {'archivos': Archivos})
