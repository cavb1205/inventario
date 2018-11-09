# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Talla(models.Model):
    nombreTalla = models.CharField(max_length=100)
    descripcionTalla = models.CharField(max_length=100)

class Categoria(models.Model):
    nombreCategoria = models.CharField(max_length=100)
    descripcionCategoria = models.CharField(max_length=100)

class Color(models.Model):
    nombreColor = models.CharField(max_length=100)
    descripcionColor = models.CharField(max_length=100)

class Producto(models.Model):
    nombreProducto = models.CharField(max_length=100)
    descripcionProducto = models.CharField(max_length=100)
    referenciaProducto = models.CharField(max_length=50)
    cantidadProducto = models.IntegerField(default=0)
    precioProducto = models.DecimalField(max_digits=10,decimal_places=2)
    tallaProducto = models.ForeignKey(Talla)
    categoriaProducto = models.ForeignKey(Categoria)
    colorProducto = models.ForeignKey(Color)
