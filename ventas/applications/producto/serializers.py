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



class ProductosPorMarcasSerializador(serializers.ModelSerializer):

    productos = serializers.SerializerMethodField()
    class Meta:
        model = Marca
        fields = (
            'id',
            'nombre',
            'productos',
        )
    
    def get_productos(self, obj):
        consulta = Producto.objects.productos_x_marcas(obj.id)
        serializador = ProductosMarcasSerializador(consulta, many=True).data
        return serializador


class ProductosMarcasSerializador(serializers.Serializer):
    codigo_barras = serializers.CharField()
    nombre = serializers.CharField()
    marca = serializers.CharField()
    precio_compra = serializers.IntegerField()
    precio_venta = serializers.IntegerField()
    cantidad = serializers.IntegerField()


#para tener encuenta, si se tienen en un mismo modelo 2 foreignkey se deben hacer 2 extra_kwargs
class ProductoHyperlinkSerilaizador(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Producto
        fields = (
            'id',
            'codigo_barras',
            'nombre',           
            'cantidad',
            'precio_compra',
            'precio_venta',
            'provedor',
        )
        extra_kwargs = {
            'provedor': {'view_name': 'producto_app:detalle_provedor', 'lookup_field': 'pk'}
        }