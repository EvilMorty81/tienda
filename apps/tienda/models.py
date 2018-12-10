from django.db import models
from apps.oferta.models import Oferta
from apps.venta.models import Venta

# Create your models here.

class Tienda(models.Model):
    numero_tienda = models.IntegerField()
    nombre_tienda = models.CharField(max_length = 50)
    direccion_tienda = models.CharField(max_length = 100)
    comuna_tienda = models.CharField(max_length = 50)
    ciudad_tienda = models.CharField(max_length = 50)
    telefono_tienda = models.IntegerField()
    email_tienda = models.EmailField()
    encargado_tienda = models.CharField(max_length = 100)
    oferta = models.ManyToManyField(Oferta)
    venta = models.ManyToManyField(Venta)