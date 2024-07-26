from django.db import models
#
from model_utils.models import TimeStampedModel
#
from .managers import ProductoManager
# Create your models here.

class Marca(TimeStampedModel):
    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.nombre



class Provedor(TimeStampedModel):
    nombre = models.CharField('Razon social', max_length=100)
    email = models.EmailField('Correo electronico', max_length=254, unique=True)
    web_site = models.URLField('Sitio web', max_length=200, blank=True)
    telefono = models.CharField('Telefono contacto', max_length=50, blank=True)

    class Meta:
        verbose_name = 'Provedor'
        verbose_name_plural = 'Provedores'
    

    def __str__(self):
        return self.nombre


class Producto(TimeStampedModel):
    codigo_barras  = models.CharField('Codigo barras', max_length=10, unique=True)
    nombre = models.CharField('Nombre producto', max_length=50)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    provedor = models.ForeignKey(Provedor, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField('Cantidad stock', default=0)
    precio_compra = models.PositiveIntegerField('Precio de compra', default=1)
    precio_venta = models.PositiveIntegerField('Precio de venta', default=2)
    disponible = models.BooleanField('Producto disponible', default=True)
    cantidad_vendida = models.PositiveIntegerField('Cantidad vendida', default=0)

    objects = ProductoManager()


    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
    

    def __str__(self):
        return self.nombre