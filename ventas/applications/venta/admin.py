from django.contrib import admin
#
from .models import DetalleVenta, Venta, CarritoCompra
# Register your models here.

class VentaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'fecha_venta',
        'cantidad_productos',
        'total_venta',
        'tipo_pago',
        'user',
        'anulada'
    )

admin.site.register(Venta, VentaAdmin)


class DetalleVentaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'venta',
        'producto',
        'cantidad',
        'precio_compra',
        'precio_venta',
        'anulado'
    )

admin.site.register(DetalleVenta, DetalleVentaAdmin)


class CarritoCompraAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo_barras',
        'cantidad',
        'producto'
    )

admin.site.register(CarritoCompra, CarritoCompraAdmin)