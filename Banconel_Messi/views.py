from django.shortcuts import render

def principal(request):
    return render(request, 'pagina_principal.html')

