from django.db import models

# Create your models here.

class Vendedor(models.Model):
    rut_vendedor = models.CharField(max_length =20)
    nombre_vendedor = models.CharField(max_length = 50)
    apellido_vendedor = models.CharField(max_length = 100)
