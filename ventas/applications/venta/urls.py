from django.urls import path, re_path, include
#
from . import views

app_name = 'venta_app'

urlpatterns = [
    path('agregar/carrito/producto/api/', views.AgregarCarritoComprasApi.as_view(), name='agregar_carrito'),
    path('lista/carrito/producto/api/', views.ListaArticulosEnCarrito.as_view(), name='lista_carrito'),
    path('aumentar/cantidad/producto/carrito/api/', views.AumentarCantidadProductoApi.as_view(), name='aumentar_cantidad_carrito'),
    path('disminuir/cantidad/producto/carrito/api/', views.DisminuirCantidadProductoApi.as_view(), name='disminuir_cantidad_carrito'),
    path('eliminar/articulo/carrito/api/', views.EliminarArticuloCarritoApi.as_view(), name='eliminar_artiuclo_carrito'),
    #
    path('crear/venta/api/', views.CrearVentaApi.as_view(), name='crear_venta'),
]
