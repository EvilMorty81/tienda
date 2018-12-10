from django.db import models
from apps.oferta.models import Oferta
from apps.tienda.models import Tienda

# Create your models here.

class Producto(models.Model):
    codigo_producto = models.IntegerField()
    categoria_producto = models.CharField(max_length = 50)
    nombre_producto = models.CharField(max_length = 100)
    descripcion_producto = models.TextField(blank=True)
    precio_producto = models.IntegerField()
    imagen_producto = models.ImageField(default='default.jpg', blank=True)
    tienda = models.ForeignKey(Tienda, null=True, blank=True, on_delete=models.CASCADE)
    oferta = models.ManyToManyField(Oferta)
    
