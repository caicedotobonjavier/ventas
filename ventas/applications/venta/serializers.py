#
from rest_framework import serializers
#
from applications.producto.models import Producto
#
from .models import CarritoCompra, Venta, DetalleVenta


# La clase `AgregarCarritoCompraSerializador` es un serializador en Python para agregar elementos a un
# carrito de compras con campos para código de barras y cantidad.
class AgregarCarritoCompraSerializador(serializers.Serializer):
    codigo_barras = serializers.CharField()
    cantidad = serializers.IntegerField()



# La clase `ListaArticulosCarritoComprasSerializador` define un serializador para una lista de compras, 
# artículos del carrito con campos para ID, código de barras, cantidad y nombre del producto.
class ListaArticulosCarritoComprasSerializador(serializers.Serializer):
    id =  serializers.IntegerField()
    codigo_barras = serializers.CharField()
    cantidad = serializers.IntegerField()
    producto = serializers.CharField()


# Esta clase de Python define un serializador para crear una venta con campos para fecha de venta y tipo de pago
class CrearVentaSerializador(serializers.Serializer):
    fecha_venta = serializers.DateField()    
    tipo_pago = serializers.CharField()