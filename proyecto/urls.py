from django.urls import path, include
from proyecto.views import *
from .models import *

urlpatterns = [
    path('principal/',vst_principal.view_principal, name='home'),
    path('crearcuenta/',vst_crear_usuario.as_view(), name='crearcuenta')
]
