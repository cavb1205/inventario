# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from .models import Producto, Talla, Color, Categoria

@admin.register(Producto)
class Producto(admin.ModelAdmin):
    list_display = ('id','nombreProducto','referenciaProducto','cantidadProducto')


@admin.register(Talla)
class Talla(admin.ModelAdmin):
    list_display = ('id','nombreTalla')