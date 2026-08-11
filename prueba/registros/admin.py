from django.contrib import admin
from django.utils.html import strip_tags
from .models import Alumnos, Comentario, ComentarioContacto

class AdministrarModelo(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ('matricula', 'nombre', 'carrera', 'turno')
    search_fields = ('matricula', 'nombre', 'carrera', 'turno')
    date_hierarchy = 'created'
    list_filter = ('carrera', 'turno')

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name__iexact='Cristopher').exists():
            return ('matricula', 'carrera', 'turno')
        elif request.user.groups.filter(name__iexact='AlumnosEditores').exists():
            return ('matricula', 'turno', 'created', 'updated')
        else:
            return ('created', 'updated')


class AdministrarComentarios(admin.ModelAdmin):
    list_display = ('id', 'comentario_limpio')
    search_fields = ('id', 'created')
    date_hierarchy = 'created'
    readonly_fields = ('created', 'id')
    ordering = ('-created',)
    list_per_page = 10
    empty_value_display = 'Sin valor'
    list_display_links = ('comentario_limpio',)

    
    def comentario_limpio(self, obj):
        return strip_tags(obj.coment)
    
    comentario_limpio.short_description = 'COMENTARIO'


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