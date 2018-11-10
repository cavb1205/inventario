# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, UpdateView, CreateView
from .models import Producto

class ProductoList(ListView):
    model = Producto


class ProductoDetail(DetailView):
    model = Producto

class ProductoCreate(CreateView):
    model = Producto
    success_url = reverse_lazy('productos:list')
    fields = ['imagenProducto','nombreProducto','descripcionProducto','referenciaProducto','cantidadProducto','precioProducto','tallaProducto','categoriaProducto','colorProducto']

class ProductoUpdate(UpdateView):
    model = Producto
    success_url = reverse_lazy('productos:list')
    fields = ['imagenProducto','nombreProducto','descripcionProducto','referenciaProducto','cantidadProducto','precioProducto','tallaProducto','categoriaProducto','colorProducto']

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy('productos:list')
