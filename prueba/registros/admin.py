from django.contrib import admin
from .models import Alumnos, Comentario, ComentarioContacto

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id','coment')
    search_fields = ('id','created')
    date_hierarchy = 'created'
    readonly_fields = ('created','id')
    ordering = ('-created',)
    list_per_page = 10
    empty_value_display = 'Sin valor'
    list_display_links = ('coment',)


class AdministrarComentariosContacto(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'mensaje', 'created')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    ordering = ('-created',)
    list_per_page = 10
    empty_value_display = 'Sin valor'


admin.site.register(Alumnos, AdministrarModelo)
admin.site.register(Comentario, AdministrarComentarios)
admin.site.register(ComentarioContacto, AdministrarComentariosContacto)