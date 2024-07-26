from django.shortcuts import render
#
from .models import CarritoCompra, Venta, DetalleVenta
#
from applications.producto.models import Producto
#
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, CreateAPIView, ListAPIView, UpdateAPIView
#
from rest_framework.views import APIView
#
from .serializers import AgregarCarritoCompraSerializador, ListaArticulosCarritoComprasSerializador
#
from rest_framework.response import Response
#
from django.shortcuts import get_object_or_404
# Create your views here.


# Esta clase de Pythonsirve para agregar productos a un carrito de compras, donde crea o
# actualiza las entradas en la base de datos según el código de barras del producto y la cantidad proporcionada.
class AgregarCarritoComprasApi(CreateAPIView):
    serializer_class = AgregarCarritoCompraSerializador

    def create(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)

        codigo_barras = serializador.validated_data['codigo_barras']
        cantidad = serializador.validated_data['cantidad']

        obj, created = CarritoCompra.objects.get_or_create(
            codigo_barras = codigo_barras,
            defaults={
                'cantidad' : cantidad,
                'producto' : Producto.objects.get(codigo_barras=codigo_barras)
            } 
        )
        if not created:
            obj.cantidad += cantidad
            obj.save()

        return Response(
            {
                'Respuesta' : f'Producto: [{Producto.objects.get(codigo_barras=codigo_barras)}] agregado al carrito'
            }
        )




# Esta clase es ListAPIView que utiliza un serializador para mostrar una lista de artículos en un carrito de compras.
class ListaArticulosEnCarrito(ListAPIView):
    serializer_class = ListaArticulosCarritoComprasSerializador
    queryset = CarritoCompra.objects.all() 


# Esta clase define un método POST que aumenta en 1 la cantidad de un producto en un carrito de compras.
class AumentarCantidadProductoApi(APIView):  
    
    def post(self, request, *args, **kwargs):
        dato = self.request.GET.get('id')
        product = get_object_or_404(CarritoCompra.objects.all(), id = dato)
        if product:
            product.cantidad += 1
            product.save()

        return Response(
            {
                'Mensaje' : f'Se aumento en 1 la cantidad del producto: [{product}]'
            }
        )



# Esta clase define un método POST para disminuir en 1 la cantidad de un producto en un carrito de compras.
class DisminuirCantidadProductoApi(APIView):  
    
    def post(self, request, *args, **kwargs):
        dato = self.request.GET.get('id')
        product = get_object_or_404(CarritoCompra.objects.all(), id = dato)
        if product:
            product.cantidad -= 1
            product.save()

        return Response(
            {
                'Mensaje' : f'Se disminuyo en 1 la cantidad del producto: [{product}]'
            }
        )


class EliminarArticuloCarritoApi(APIView):  
    
    def post(self, request, *args, **kwargs):
        dato = self.request.GET.get('id')
        product = get_object_or_404(CarritoCompra.objects.all(), id = dato)
        if product:
            product.delete()

        return Response(
            {
                'Mensaje' : f'Se elimino el articulo: [{product}] del carrito de compras'
            }
        )