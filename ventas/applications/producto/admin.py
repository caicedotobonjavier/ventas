from django.contrib import admin
#
from .models import Marca, Producto, Provedor
# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
    )

admin.site.register(Marca, MarcaAdmin)


class ProvedorAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'nombre',
        'email',
        'telefono',
        'web_site',
    )

admin.site.register(Provedor, ProvedorAdmin)


class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'codigo_barras',
        'nombre',
        'marca',
        'provedor',
        'cantidad',
        'precio_compra',
        'precio_venta',
        'cantidad_vendida',
        'disponible',
    )

admin.site.register(Producto, ProductoAdmin)
    