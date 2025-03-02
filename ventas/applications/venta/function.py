#
from applications.producto.models import Producto
#
from .models import CarritoCompra, Venta, DetalleVenta
#
from rest_framework.response import Response

def crear_venta(self, **datos_venta):
    """
    La función crea un nuevo registro de ventas con el detalle de los productos vendidos y actualiza el total
    ventas, cantidad y número de productos.
    :return: La función `crear_venta` devuelve el objeto `Venta` recién creado, que representa
    una transacción de venta con detalles de los productos vendidos.
    """
    productos_carrito = CarritoCompra.objects.all()

    if len(productos_carrito) > 0:

        nueva_venta = Venta.objects.create(
            fecha_venta = datos_venta['fecha_venta'],
            cantidad_productos = datos_venta['cantidad_productos'],
            total_venta =  datos_venta['total_venta'],
            tipo_pago = datos_venta['tipo_pago'],
            user = datos_venta['user']
        )
        
        lista_detalle = []
        productos_vendidos = []
        cantidad_producto = 0
        valor_total = 0

        for productos in productos_carrito:
            detalle = DetalleVenta(
                venta = nueva_venta,
                producto = productos.producto,
                cantidad = productos.cantidad,
                precio_compra = productos.producto.precio_compra,
                precio_venta = productos.producto.precio_venta
            )

            lista_detalle.append(detalle)            
            cantidad_producto += productos.cantidad
            valor_total += productos.producto.precio_venta * productos.cantidad

            productos.producto.cantidad_vendida += productos.cantidad
            productos.producto.cantidad -= productos.cantidad
            productos_vendidos.append(productos.producto)

        DetalleVenta.objects.bulk_create(
            lista_detalle
        )

        Producto.objects.bulk_update(
            productos_vendidos,
            ['cantidad_vendida', 'cantidad']
        )

        nueva_venta.cantidad_productos = cantidad_producto
        nueva_venta.total_venta = valor_total
        nueva_venta.save()

        productos_carrito.delete()

        return nueva_venta