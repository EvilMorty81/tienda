from django.db import models
from django.utils import timezone

# Create your models here.

class Venta(models.Model):
    numero_venta = models.IntegerField(primary_key=True)
    fecha_venta = models.DateTimeField(default=timezone.now)
    cantidad_venta = models.IntegerField()
    subtotal_venta = models.IntegerField()
    total_venta = models.IntegerField()
    comentario_venta = models.TextField(blank=True)

