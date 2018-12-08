from django.db import models

# Create your models here.
class Oferta(models.Model):
    precio_oferta = models.IntegerField()
    comentario_oferta = models.TextField(blank=True)