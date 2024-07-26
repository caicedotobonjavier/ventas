#
from rest_framework import serializers
#
from applications.producto.models import Producto
#
from .models import CarritoCompra, Venta, DetalleVenta


class AgregarCarritoCompraSerializador(serializers.Serializer):
    codigo_barras = serializers.CharField()
    cantidad = serializers.IntegerField()



class ListaArticulosCarritoComprasSerializador(serializers.Serializer):
    id =  serializers.IntegerField()
    codigo_barras = serializers.CharField()
    cantidad = serializers.IntegerField()
    producto = serializers.CharField()