from inicio import views
from django.contrib import admin
from django.urls import path
from django.conf import settings
from registros import views as views_registros 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views_registros.registros, name='principal'),
    path('nombre/', views.nombre, name='nombre'),
    path('contacto/', views_registros.registrar, name='contacto'),
    path('registrar/', views_registros.registrar, name='registrar'),
    path('formulario/', views.formulario, name='formulario'),
    path('consultarComentario/', views_registros.consultarComentario, name='consultarComentario'),
    path('formEditarComentario/<int:id>/', views_registros.consultarComentarioIndividual, name='ConsultaIndividual'),
    path('editarComentario/<int:id>/', views_registros.editarComentarioContacto, name='Editar'),
    path('comentario/eliminar/<int:id>/', views_registros.eliminarComentario, name='eliminarComentario'),
    path('consultas/', views.consultas, name='consultas'),
    path('consultas1/', views.consultar1, name='consultas1'),
    path('consultas2/', views.consultar2, name='consultas2'),
    path('consultas3/', views.consultar3, name='consultas3'),
    path('consultas4/', views.consultar4, name='consultas4'),
    path('consultas5/', views.consultar5, name='consultas5'),
    path('consultas6/', views.consultar6, name='consultas6'),
    path('consultas7/', views.consultar7, name='consultas7'),
    path('consultas8/', views.consultar8, name='consultas8'),
    path('consultasSQL1/', views.consultasSQL1, name='consultasSQL1'),
    path('consultasSQL2/', views.consultasSQL2, name='consultasSQL2'),
    path('consultasSQL3/', views.consultasSQL3, name='consultasSQL3'),
    path('consultasSQL4/', views.consultasSQL4, name='consultasSQL4'),
    path('consultasSQL5/', views.consultasSQL5, name='consultasSQL5'),
    path ('subir', views_registros.archivos, name='Subir'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)