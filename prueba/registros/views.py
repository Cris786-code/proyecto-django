from django.shortcuts import render, redirect, get_object_or_404
from .models import Alumnos, ComentarioContacto
from .forms import ComentarioContactoForm

def registros(request):
    alumnos = Alumnos.objects.all()
    return render(request, "registros/principal.html", {'alumnos': alumnos})

def registrar(request):
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})
    
    form = ComentarioContactoForm()
    return render(request, "registros/contacto.html", {'form': form})


def consultarComentario(request):
    comentarios = ComentarioContacto.objects.all()
    return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})



def contacto(request):
    return render(request, "registros/contacto.html")


def editarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, pk=id)
    if request.method == 'POST':
        form = ComentarioContactoForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            comentarios = ComentarioContacto.objects.all()
            return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})
    else:
        form = ComentarioContactoForm(instance=comentario)
    return render(request, 'registros/editarComentario.html', {'form': form, 'comentario': comentario})


def eliminarComentario(request, id):
    comentario = get_object_or_404(ComentarioContacto, pk=id)
    if request.method == 'POST':
        comentario.delete()
        comentarios = ComentarioContacto.objects.all()
        return render(request, "registros/consultarComentario.html", {'comentarios': comentarios})
    return render(request, 'registros/confirmarEliminarComentario.html', {'comentario': comentario})