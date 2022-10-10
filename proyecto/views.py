from django.shortcuts import render, HttpResponsePermanentRedirect
from django.views.generic import *
from django.contrib.auth.models import User 
from django.urls import reverse_lazy
from proyecto.forms import *

class vst_principal():
    def view_principal(request):
        return render(request,'pagina_principal.html')

class vst_crear_usuario(CreateView):
    model= User
    template_name= "pagina_crear_cuenta.html"
    form_class = Nameform
    success_url= reverse_lazy('home')

