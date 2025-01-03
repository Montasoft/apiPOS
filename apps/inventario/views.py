from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Categoria, SubCategoria, EstadoProducto, Producto
from .serializers import CategoriaDetalleSerializer, CategoriaListaSerializer, EstadoProductoDetalleSerializer, EstadoProductoListaSerializer, ProductoDetalleSerializer, ProductoListaSerializer, SubCategoriaDetalleSerializer, SubCategoriaListaSerializer
from apps.baseapp.views import BaseCreateUpdateView, BaseDeleteView, BaseListView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

from rest_framework.pagination import PageNumberPagination

class CustomPagination(PageNumberPagination):
    page_size = 50  # Tamaño por página
    page_size_query_param = 'page_size'
    max_page_size = 100



########################################################################################
########  VISTAS GENÉRICAS PARA LISTA DE CADA MODELO ###################################
########################################################################################

class CategoriaListView(BaseListView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaListaSerializer

class SubCategoriaListView(BaseListView):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaListaSerializer

class EstadoProductoListView(BaseListView):
    queryset = EstadoProducto.objects.all()
    serializer_class = EstadoProductoListaSerializer

class ProductoListView(BaseListView):
    queryset = Producto.objects.all()
    serializer_class = ProductoListaSerializer
    pagination_class = CustomPagination
    
    #filtros
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['categoria', 'nombre']
    ordering_fields = ['nombre', 'pricio']

########################################################################################
########  VISTAS GENÉRICAS PARA DETALLES DE CADA MODELO ################################
########################################################################################
 
class CategoriaDetailView(RetrieveAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetalleSerializer

class SubCategoriaDetailView(RetrieveAPIView):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaDetalleSerializer

class EstadoProductoDetailView(RetrieveAPIView):
    queryset = EstadoProducto.objects.all()
    serializer_class = EstadoProductoDetalleSerializer

class ProductoDetailView(RetrieveAPIView):
    queryset = Producto.objects.all()
    serializer_class = ProductoDetalleSerializer

########################################################################################
########  VISTAS GENÉRICAS PARA CREAR O ACTUALIZAR CADA MODELO #########################
########################################################################################

class CategoriaCreateUpdateView(BaseCreateUpdateView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaDetalleSerializer

class SubCategoriaCreateUpdateView(BaseCreateUpdateView):
    queryset = SubCategoria.objects.all()
    serializer_class = SubCategoriaDetalleSerializer

class EstadoProductoCreateUpdateView(BaseCreateUpdateView):
    queryset = EstadoProducto.objects.all()
    serializer_class = EstadoProductoDetalleSerializer

class ProductoCreateUpdateView(BaseCreateUpdateView):
    queryset = Producto.objects.all()
    serializer_class = ProductoDetalleSerializer

########################################################################################
########  VISTAS GENÉRICAS PARA MARCAR COMO ELIMINADO CADA MODELO ######################
########################################################################################


class CategoriaDeleteView(BaseDeleteView):
    model = Categoria
    serializer_class = CategoriaDetalleSerializer

class SubCategoriaDeleteView(BaseDeleteView):
    model = SubCategoria
    serializer_class = SubCategoriaDetalleSerializer

class EstadoProductoDeleteView(BaseDeleteView):
    model = EstadoProducto
    serializer_class = EstadoProductoDetalleSerializer

class ProductoDeleteView(BaseDeleteView):
    model = Producto
    serializer_class = ProductoDetalleSerializer
