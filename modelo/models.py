from django.db import models

class Clientes(models.Model):
    cliente_id = models.AutoField(primary_key = True)
    nombre = models.CharField(max_length=30,null = False)
    cedula = models.CharField(max_length=10,null = False)
    def __str__(self):
        return self.cedula+''


class Servicios(models.Model):
    servicio_id = models.AutoField(primary_key = True)
    tipo = models.CharField(max_length=25,null = False)
    cliente = models.CharField(max_length=25,null = False)
    precio = models.FloatField(max_length=10,null = False)
    uso = models.IntegerField()

