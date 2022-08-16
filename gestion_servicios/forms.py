from django import forms
from modelo.models import Servicio

class ServicioFormulario(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ["tipo","cliente","precio","uso"]
        widgets = {
            'tipo': forms.TextInput(attrs={'placeholder':'Ingrese tipo', 'class': 'form-control'}),
            'cliente': forms.TextInput(attrs={'placeholder':'Ingrese cedula', 'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'placeholder':'Ingrese precio', 'class': 'form-control'}),
            'uso': forms.NumberInput(attrs={'placeholder':'Ingrese uso en horas', 'class': 'form-control'}),
        }