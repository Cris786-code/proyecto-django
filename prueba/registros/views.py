from django.shortcuts import render
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