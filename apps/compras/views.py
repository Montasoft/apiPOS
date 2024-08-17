from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Compra, EstadoCompra, Proveedor, CompraDetalle, PagoCompra
from .serializers import CompraListaSerializer, CompraDetalleListaSerializer, EstadoCompraListaSerializer, EstadoCompraDetalleSerializer, ProveedorListaSerializer, ProveedorDetalleSerializer, PagoCompraListaSerializer
from apps.baseapp.views import BaseListView


########################################################################################
########  VISTAS GENÉRICAS PARA LISTA DE CADA MODELO ################################
########################################################################################

class EstadoCompraListView(BaseListView):
    queryset = EstadoCompra.objects.all()
    serializer_class = EstadoCompraListaSerializer


class ProveedorListView(BaseListView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorListaSerializer


class CompraListView(BaseListView):
    queryset = Compra.objects.all()
    serializer_class = CompraListaSerializer


class CompraDetalleListView(BaseListView):
    queryset = CompraDetalle.objects.all()
    serializer_class = CompraDetalleListaSerializer


class PagoCompraListView(BaseListView):
    queryset = PagoCompra.objects.all()
    serializer_class = PagoCompraListaSerializer

########################################################################################
########  VISTAS GENÉRICAS PARA DETALLES DE CADA MODELO ################################
########################################################################################
 

class ProveedorDetailView(RetrieveAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorDetalleSerializer

