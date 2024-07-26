from django.db import models
#
from model_utils.models import TimeStampedModel
#
from applications.producto.models import Producto
#
from django.conf import settings
# Create your models here.


class Venta(TimeStampedModel):

    EFECTIVO = '0'
    TARJETA = '1'
    CHEQUE = '2'
    BONO = '3'
    OTRO = '4'

    TIPO_PAGO_CHOICES = (
        (EFECTIVO, 'Efectivo'),
        (TARJETA, 'Tarjeta'),
        (CHEQUE, 'Cheque'),
        (BONO, 'Bono'),
        (OTRO, 'Otro'),
    )

    fecha_venta = models.DateField('Fecha de Venta')
    cantidad_productos = models.PositiveIntegerField('Cantidad de productos')
    total_venta = models.PositiveIntegerField('Total de la venta')
    anulada = models.BooleanField('Venta anulada', default=False)
    tipo_pago = models.CharField('Tipo de pago', max_length=1, choices=TIPO_PAGO_CHOICES, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='venta_user', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
    

    def __str__(self):
        return '['+str(self.id)+'] -' + str(self.fecha_venta)



class DetalleVenta(TimeStampedModel):
    venta = models.ForeignKey(Venta, related_name='detalle_ventas', verbose_name='Codigo de Venta', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='detalle_producto', on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField('Cantidad')
    precio_compra = models.PositiveIntegerField('Precio de compra')
    precio_venta = models.PositiveIntegerField('Precio de venta')
    anulado = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Detalle Venta'
        verbose_name_plural = 'Detalle Ventas'
    

    def __str__(self):
        return str(self.id) + ' - ' + str(self.producto.nombre)



class CarritoCompra(TimeStampedModel):
    codigo_barras = models.CharField('Codigo de barras', max_length=10, unique=True)
    cantidad = models.PositiveIntegerField('Cantidad')
    producto = models.ForeignKey(Producto, related_name='producto_carrito', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Carrito de Compra'
        verbose_name_plural = 'Carrito de Compras'
    

    def __str__(self):
        return str(self.producto.nombre)