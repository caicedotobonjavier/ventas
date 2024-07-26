from django.urls import path, re_path, include
#
from . import views

app_name = 'producto_app'

urlpatterns = [
    path('api/marca/create/', views.CrearMarcaApi.as_view(), name='crear_marca'),
    path('api/provedor/create/', views.CrearProvedorApi.as_view(), name='crear_provedor'),
    path('api/producto/create/', views.CrearProductoApi.as_view(), name='crear_producto'),
    path('api/marcas/list/', views.LIstaMarcasApi.as_view(), name='lista_marcas'),
    path('api/producto/list/', views.LIstaProductosApi.as_view(), name='lista_productos'),
    path('api/provedores/list/', views.LIstaProvedoressApi.as_view(), name='lista_provedores'),
    path('api/marcas/productos/list/', views.ListaMarcasConProductos.as_view(), name='marcas_productos'),
    path('api/provedor/detalle/<pk>/', views.DetallesProvedorApi.as_view(), name='detalle_provedor'),
    path('api/productos/link/provedores/', views.ProductosListaHyperLinkApi.as_view(), name='producots_link'),
]
