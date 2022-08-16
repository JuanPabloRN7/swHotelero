from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from modelo.models import Servicios
from .forms import FormularioServicios
from django.contrib.auth.models import User, Group

# Create your views here.
##def ingresarServicios(request):
    ##listaCliente = Servicios.objects.all().order_by('cliente')
    ##return render(request,"guiRegistrarServicio.html")

def ingresarServicios(request):
    formulario_Servicios = FormularioServicios(request.POST)

    if request.method == 'POST':
        if formulario_Servicios.is_valid():
            servicio = Servicios()
            datos_servicio = formulario_Servicios.cleaned_data
            servicio.tipo = datos_servicio.get('tipo')
            servicio.cliente = datos_servicio.get('cliente')
            servicio.precio = datos_servicio.get('precio')
            servicio.uso = datos_servicio.get('uso')
            servicio.save()
        
            
            ##return redirect(ingresarServicios)
    return render(request,'guiRegistrarServicio.html', locals())

    