from django.shortcuts import render
from modelo.models import Servicio, Cliente
from .forms import ServicioFormulario

# Create your views here.
def registrar(request):
    formulario_servicio = ServicioFormulario(request.POST)
    if request.method == 'POST' and formulario_servicio.is_valid():
        servicio = Servicio()
        datos_servicio = formulario_servicio.cleaned_data
        servicio.tipo = datos_servicio.get('tipo')
        servicio.cliente = datos_servicio.get('cliente')
        servicio.precio = datos_servicio.get('precio')
        servicio.uso = datos_servicio.get('uso')
        servicio.save()
    else:
        print("No validos")
    return render(request, 'servicios/guiRegistrarServicio.html', locals())