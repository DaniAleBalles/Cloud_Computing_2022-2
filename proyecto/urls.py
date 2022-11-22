from django.urls import path, include
from proyecto.views import *
from .models import *

urlpatterns = [
    path('principal/',vst_principal.view_principal, name='home'),
    path('crearcuenta/',vst_registro, name='crearcuenta'),
    path('ingresar/',vst_ingreso, name='ingreso'),
    path('',vst_cerrar, name='cerrar'),
    path('pais/',vst_pais.as_view(), name='pais'),
    path('ciudad/',vst_ciudad.as_view(), name='ciudad'),
    path('usuario/<id>',vst_usuario.as_view(), name='usuario'),
    path('destinatario/',vst_agregar_dest.as_view(), name='destinatario'),
    path('list_Dest/',vst_listdest.as_view(), name='listadestinatarios'),
    path('del_Dest/<int:pk>',vst_deldest.as_view(), name='Eliminar'),
    path('moneda',vst_moneda.as_view(), name='moneda'),    
    path('monedalist/',vst_list_moneda.as_view(), name='monedalist'),
    path('monedaupd/<int:pk>',vst_upd_moneda.as_view(), name='editar'),
    path('monedaarchi/<id>',vst_archi_moneda.as_view(), name='archivar'),
    path('monedaarchivar/<id>',vst_archivar_moneda.as_view(), name='archivarno'),
    path('transaccion/',vst_transacciones.as_view(), name='transaccion'),
    path('transacciones/',vst_moneda_plus.as_view(), name='moneda_plus')
]
