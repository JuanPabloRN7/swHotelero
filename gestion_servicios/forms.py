from django import forms
from modelo.models import Servicios,Clientes

class FormularioServicios(forms.Form):
    tipo = forms.CharField(max_length=100)  
    cliente = forms.ModelChoiceField(queryset=Clientes.objects.all())
    precio = forms.CharField(max_length=100)
    uso = forms.CharField(max_length=100)

