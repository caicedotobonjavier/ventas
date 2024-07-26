from django.urls import path, re_path, include
#
from . import views

app_name = 'producto_app'

urlpatterns = [
    path('api/marca/create/', views.CrearMarcaApi.as_view(), name='crear_marca'),
    path('api/provedor/create/', views.CrearProvedorApi.as_view(), name='crear_provedor'),
    path('api/producto/create/', views.CrearProductoApi.as_view(), name='crear_producto'),
]
