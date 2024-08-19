from django.shortcuts import render

from rest_framework import generics
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Compra, EstadoCompra, Proveedor, CompraDetalle, PagoCompra
from .serializers import CompraDetalleDetalleSerializer, CompraDetalleSerializer, CompraListaSerializer, CompraDetalleListaSerializer, EstadoCompraListaSerializer, EstadoCompraDetalleSerializer, PagoCompraDetalleSerializer, ProveedorListaSerializer, ProveedorDetalleSerializer, PagoCompraListaSerializer
from apps.baseapp.views import BaseCreateUpdateView, BaseDeleteView, BaseListView


########################################################################################
########  VISTAS GENÉRICAS PARA LISTA DE CADA MODELO ###################################
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


class PagoCompraListView(BaseListView):
    queryset = PagoCompra.objects.all()
    serializer_class = PagoCompraListaSerializer


class CompraDetalleListView(BaseListView):
    queryset = CompraDetalle.objects.all()
    serializer_class = CompraDetalleListaSerializer


########################################################################################
########  VISTAS GENÉRICAS PARA DETALLES DE CADA MODELO ################################
########################################################################################
 

class EstadoCompraDetailView(RetrieveAPIView):
    queryset = EstadoCompra.objects.all()
    serializer_class = EstadoCompraDetalleSerializer

class ProveedorDetailView(RetrieveAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorDetalleSerializer

class CompraDetailView(RetrieveAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraDetalleSerializer

class CompraDetalleDetailView(RetrieveAPIView):
    queryset = CompraDetalle.objects.all()
    serializer_class = CompraDetalleDetalleSerializer

class PagoCompraDetailView(RetrieveAPIView):
    queryset = PagoCompra.objects.all()
    serializer_class = PagoCompraDetalleSerializer

########################################################################################
########  VISTAS GENÉRICAS PARA CREAR O ACTUALIZAR CADA MODELO #########################
########################################################################################


class EstadoCompraCreateUpdateView(BaseCreateUpdateView):
    queryset = EstadoCompra.objects.all()
    serializer_class = EstadoCompraDetalleSerializer

class ProveedorCreateUpdateView(BaseCreateUpdateView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorDetalleSerializer

class PagoCompraCreateUpdateView(BaseCreateUpdateView):
    queryset = PagoCompra.objects.all()
    serializer_class = PagoCompraDetalleSerializer

class CompraCreateUpdateView(BaseCreateUpdateView):
    queryset = Compra.objects.all()
    serializer_class = CompraDetalleSerializer

class CompraDetalleCreateUpdateView(BaseCreateUpdateView):
    queryset = CompraDetalle.objects.all()
    serializer_class = CompraDetalleDetalleSerializer


########################################################################################
########  VISTAS GENÉRICAS PARA MARCAR COMO ELIMINADO CADA MODELO ######################
########################################################################################


class EstadoCompraDeleteView(BaseDeleteView):
    model = EstadoCompra
    serializer_class = EstadoCompraDetalleSerializer

class ProveedorDeleteView(BaseDeleteView):
    model = Proveedor
    serializer_class = ProveedorDetalleSerializer

class PagoCompraDeleteView(BaseDeleteView):
    model = PagoCompra
    serializer_class = PagoCompraDetalleSerializer

class CompraDeleteView(BaseDeleteView):
    model = Compra
    serializer_class = CompraDetalleSerializer

class CompraDetalleDeleteView(BaseDeleteView):
    model = CompraDetalle
    serializer_class = CompraDetalleDetalleSerializer

