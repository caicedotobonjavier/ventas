from django.shortcuts import render
#
from .models import Marca, Provedor, Producto
#
from rest_framework.generics import CreateAPIView
#
from rest_framework.views import APIView
#
from .serializers import MarcaSerializador, ProvedorSerializador, ProductoSerializador
#
from rest_framework.response import Response
# Create your views here.


class CrearMarcaApi(CreateAPIView):
    serializer_class = MarcaSerializador
    #queryset = Marca.objects.all()
    

    def create(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)

        Marca.objects.create(
            nombre = serializador.validated_data['nombre']
        )
        
        return Response(
            {
                'Mensaje' : 'Guardado Correctamente'
            }
        )



class CrearProvedorApi(CreateAPIView):
    serializer_class = ProvedorSerializador
    #queryset = Provedor.objects.all()

    def create(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)

        Provedor.objects.create(
            nombre = serializador.validated_data['nombre'],
            email = serializador.validated_data['email'],
            web_site = serializador.validated_data['web_site'],
            telefono = serializador.validated_data['telefono']
        )
        
        return Response(
            {
                'Respuesta' : 'Se creo correctamente el provedor'
            }
        )



class CrearProductoApi(CreateAPIView):
    serializer_class = ProductoSerializador
    #queryset = Producto.objects.all()

    def create(self, request, *args, **kwargs):
        serializador = self.serializer_class(data=request.data)
        serializador.is_valid(raise_exception=True)

        Producto.objects.create(
            codigo_barras = serializador.validated_data['codigo_barras'],
            nombre = serializador.validated_data['nombre'],
            marca = Marca.objects.get(id=serializador.validated_data['marca']),
            provedor = Provedor.objects.get(id=serializador.validated_data['provedor']),
            cantidad = serializador.validated_data['cantidad'],
            precio_compra = serializador.validated_data['precio_compra'],
            precio_venta = serializador.validated_data['precio_venta']
        )


        return Response(
            {
                'Mensaje' : 'Producto creado correctamente'
            }
        )