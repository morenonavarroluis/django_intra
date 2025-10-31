from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio , name="inicio"),
    path('loggi', loggi, name='loggi'),
    path('admi', admi , name="admi"),
    path('usuario', usuario, name="usuario"),
    path('add_noticia', add_noticia, name="add_noticia"),
    path('soporte', soporte, name="soporte"),
    path('solicitud_soport', solicitud_soport, name="solicitud_soport"),
    path('registrar_usuarios', registrar_usuarios, name='registrar_usuarios'),
    path('registrar_rol', registrar_rol, name='registrar_rol'),
    path('cerrar-sesion/', exit, name='cerrar_sesion')
]
