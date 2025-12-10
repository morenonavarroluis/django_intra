from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio , name="inicio"),
    path('loggi', loggi, name='loggi'),
    path('admi', admi , name="admi"),
    path('usuario', usuario, name="usuario"),
    path('add_noticia', add_noticia, name="add_noticia"),
    path('soporte', soporte, name="soporte"),
    path('reporte/<int:ID_REPORT>/', asignar_report, name="reporte"),
    path('export/',export_pdf, name="export-pdf" ),
    path('solicitud_soport', solicitud_soport, name="solicitud_soport"),
    path('registrar_usuarios', registrar_usuarios, name='registrar_usuarios'),
    path('registrar_rol', registrar_rol, name='registrar_rol'),
    path('eliminar_usuario/<int:user_id>/', eliminar_usuario, name='eliminar_usuario'),
    path('editar_usuario/<int:user_id>/', editar_usuario, name='editar_usuario'),
    path('recibo/export/', export_receipt_pdf, name="export-receipt-pdf"),
    # path('recibo/export/<int:recibo_id>/', export_receipt_pdf, name="export-receipt-pdf-id"),
    path('cerrar-sesion/', exit, name='cerrar_sesion')
]
