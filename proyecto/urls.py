from django.urls import path, include
from proyecto.views import *

urlpatterns = [
    path('principal/',vst_principal.view_principal, name='home')
]
