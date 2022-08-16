from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from modelo.models import Servicio, Cliente
from .forms import ServicioFormulario
from django.shortcuts import render
from django.contrib.auth.models import User, Group

# Create your views here.
def registrar(request):
    formulario_servicio = ServicioFormulario(request.POST)
    listaCliente = Cliente.objects.all()
    if request.method == 'POST':
        if formulario_servicio.is_valid():
            servicio = Servicio()
            datos_servicio = formulario_servicio.cleaned_data
            servicio.tipo = datos_servicio.get('tipo')
            servicio.cliente = datos_servicio.get('cliente')
            servicio.precio = datos_servicio.get('precio')
            servicio.uso = datos_servicio.get('uso')
            servicio.save()
    return render(request, 'servicios/guiRegistrarServicio.html', locals())