from django.db import models
from apps.tienda.models import Tienda
from apps.venta.models import Venta

# Create your models here.

class Vendedor(models.Model):
    rut_vendedor = models.CharField(max_length =20)
    nombre_vendedor = models.CharField(max_length = 50)
    apellido_vendedor = models.CharField(max_length = 100)
    tienda = models.OneToOneField(Tienda, null=True, blank=True, on_delete=models.CASCADE)
    venta = models.ManyToManyField(Venta)
