#
from rest_framework import serializers
#
from .models import Marca, Producto, Provedor


class MarcaSerializador(serializers.Serializer):    
    nombre = serializers.CharField()


class ProvedorSerializador(serializers.Serializer):
    nombre = serializers.CharField()    
    email = serializers.EmailField()
    web_site = serializers.URLField()
    telefono = serializers.CharField()



class ProductoSerializador(serializers.Serializer):
    codigo_barras = serializers.CharField()
    nombre = serializers.CharField()
    marca = serializers.CharField()
    provedor = serializers.CharField()
    cantidad = serializers.IntegerField()
    precio_compra = serializers.IntegerField()
    precio_venta = serializers.IntegerField()
    cantidad = serializers.IntegerField()