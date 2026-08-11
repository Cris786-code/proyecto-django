import datetime
from django.shortcuts import render
from registros.models import Alumnos, Comentario, ComentarioContacto

def principal(request):
     return render(request, "inicio/principal.html")

def nombre(request):
    return render(request, "inicio/nombre.html")

def contacto(request):
    return render(request ,"inicio/contacto.html" )
   
def formulario(request):
    return render(request , "inicio/formulario.html")

def consultas(request):
    alumnos = Alumnos.objects.all()
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar1(request):
    alumnos = Alumnos.objects.filter(carrera='TI')
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar2(request):
    alumnos = Alumnos.objects.filter(carrera='TI').filter(turno='Matutino')
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar3(request):
    alumnos = Alumnos.objects.all().only('matricula', 'nombre', 'carrera', 'turno', 'imagen')
    return render(request, "inicio/consultas.html", {'alumnos': alumnos})

def consultar4(request):
        fecha_inicio = datetime.date(2026, 6, 20)
        fecha_fin = datetime.date(2026, 8, 4)
        comentarios = Comentario.objects.filter(created__date__range=(fecha_inicio, fecha_fin))
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})

def consultar5(request):
        comentarios = Comentario.objects.filter(coment__icontains='buena')
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})

def consultar6(request):
        comentarios = Comentario.objects.filter(alumno__nombre__icontains='juan')
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})

def consultar7(request):
        comentarios = ComentarioContacto.objects.filter(mensaje__istartswith='Hola')
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})

def consultar8(request):
        comentarios = ComentarioContacto.objects.filter(mensaje__iendswith='gracias')
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})

def consultasSQL1(request):
        comentarios = Comentario.objects.raw(
            "SELECT id, coment, alumno_id, created FROM registros_comentario "
            "WHERE created BETWEEN '2026-06-20' AND '2026-08-04 23:59:59'"
        )
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})

def consultasSQL2(request):
        comentarios = Comentario.objects.raw(
            "SELECT id, coment, alumno_id, created FROM registros_comentario "
            "WHERE coment LIKE '%buena%'"
        )
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})

def consultasSQL3(request):
        comentarios = Comentario.objects.raw(
            "SELECT c.id, c.coment, c.alumno_id, c.created "
            "FROM registros_comentario c "
            "INNER JOIN registros_alumnos a ON c.alumno_id = a.id "
            "WHERE LOWER(a.nombre) LIKE '%juan%'"
        )
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})

def consultasSQL4(request):
        comentarios = ComentarioContacto.objects.raw(
            "SELECT id, mensaje, usuario, created FROM registros_comentariocontacto "
            "WHERE mensaje LIKE 'Hola%'"
        )
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})

def consultasSQL5(request):
        comentarios = ComentarioContacto.objects.raw(
            "SELECT id, mensaje, usuario, created FROM registros_comentariocontacto "
            "WHERE mensaje LIKE '%gracias'"
        )
        return render(request, "inicio/consultas.html", {'comentarios': comentarios})