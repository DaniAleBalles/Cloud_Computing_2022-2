from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import *
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate,login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from django.contrib import messages
from proyecto.forms import *
from proyecto.models import *

class vst_principal():
    def view_principal(request):
        return render(request,'pagina_principal.html')

def vst_registro(request):
    data = {
        'form': Nameform()
    }
    if request.method == "POST":
        formulario = Nameform(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            instance = Usuario(User_id=User.objects.latest('id'))
            instance.save()
            usuario = formulario.cleaned_data.get('username')
            password = formulario.cleaned_data.get('password')
            usuario = authenticate(username=usuario, password=password)
            return redirect(to='usuario')
        data["form"] = formulario
    return render(request,'pagina_agregar_USUARIO.html', data )

class vst_pais(CreateView):
    model= Paises
    form_class= FormPaises
    template_name='pagina_agregar_moneda.html'
    success_url= reverse_lazy('home')

class vst_ciudad(CreateView):
    model= Ciudades
    form_class= FormCiudades
    template_name='pagina_agregar_ciudad.html'
    success_url= reverse_lazy('home')

def vst_ingreso(solicitud):
    #Función que redirige al usuario si puede ingresar
    if solicitud.method == "POST":
        form = AuthenticationForm(solicitud, data=solicitud.POST)
        if form.is_valid():
            nombreusu = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(solicitud, username = nombreusu, password = password)
            if usuario is not None:
                login(solicitud, usuario)
                messages.success(solicitud,F"Bienvenido {nombreusu}")
                return redirect(to='home')
            else:
                messages.success(solicitud,F"Los datos son incorrectos")
        else:
            messages.success(solicitud,F"Los datos son incorrectos")
    form = AuthenticationForm()
    return render(solicitud,'pagina_inicio.html', {"form": form} )

def vst_cerrar(solicitud):
    logout(solicitud)
    messages.success(solicitud,"tu sesión ha cerrado ")
    return redirect(to='home')

class vst_usuario(UpdateView):
    model= Usuario
    form_class = FormUsuario
    template_name='pagina_agregar_moneda.html'
    success_url= reverse_lazy('home')

class vst_agregar_dest(CreateView):
    model= Destinatario
    form_class= FormDestinatarios
    template_name= 'pagina_agregar_moneda.html'
    success_url= reverse_lazy('home')

class vst_listdest(ListView):
    model= Destinatario
    template_name = 'pagina_listar_destinatario.html'

    def get_queryset(self):
        return Destinatario.objects.all()

class vst_deldest(DeleteView):
    model=Destinatario
    template_name= 'pagina_eliminar_dest.html'
    success_url= reverse_lazy('listadestinatarios')

class vst_moneda(CreateView):
    model=Monedas
    form_class= FormMonedas
    template_name= 'pagina_agregar_moneda.html'
    success_url = reverse_lazy('home')

class vst_list_moneda(ListView):
    model=Monedas
    template_name= 'pagina_listar_moneda.html'

    def get_queryset(self):
        return Monedas.objects.all()

class vst_upd_moneda(UpdateView):
    model=Monedas
    form_class= FormMonedas
    template_name= 'pagina_agregar_moneda.html'
    success_url = reverse_lazy('home')

class vst_archi_moneda(TemplateView):
    model = Monedas
    template_name = 'pagina_archivar_moneda.html'
    success_url = reverse_lazy('home')

    def post(self,request,id):
        moneda= Monedas.objects.get(id_Moneda=id)
        if request.method == 'POST':
            Monedas.archivo= True
            Monedas.save()
        return HttpResponseRedirect(self.success_url)





