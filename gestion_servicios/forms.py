from dataclasses import fields
from django import forms
from modelo.models import Servicio

class ServicioFormulario(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = ['tipo','cliente','precio','uso']