from django.db import models

# Create your models here.
class Evento(models.Model):
    listaTiposE=(
        ('Conferencia'),('Convención'),('Celebración'),('Boda'),('Banquete')
    )
    evento_id = models.AutoField(primary_key=True)
    tipoEvento = models.CharField(max_length=20, choices=listaTiposE)
    fechaInicio = models.DateTimeField(auto_now_add=True, null = False)
    fechaFin = models.DateTimeField(auto_now_add=True, null = False)
    numInvitados = models.IntegerField(max_length=100, null = False)