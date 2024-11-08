from django.shortcuts import render

from apps.inventario.models import Producto
from rest_framework import generics, status
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination

from django.core.exceptions import ValidationError

from rest_framework.response import Response
from .models import Compra, EstadoCompra, EstadoPedido, Pedido, Proveedor, CompraDetalle, PagoCompra
from .serializers import CompraDetalleDetalleSerializer, CompraDetalleSerializer, CompraListaSerializer, CompraDetalleListaSerializer, EstadoCompraListaSerializer, EstadoCompraDetalleSerializer, EstadoPedidoDetalleSerializer, EstadoPedidoListaSerializer, PagoCompraDetalleSerializer, PedidoDetalleSerializer, PedidoListaSerializer, PedidoSolicitadoListaSerializer, ProveedorListaSerializer, ProveedorDetalleSerializer, PagoCompraListaSerializer
from apps.baseapp.views import BaseCreateUpdateView, BaseDeleteView, BaseListView

import logging
logger = logging.getLogger(__name__)

########################################################################################
########  VISTAS GENÉRICAS PARA LISTA DE CADA MODELO ###################################
########################################################################################

class EstadoCompraListView(BaseListView):
    queryset = EstadoCompra.objects.all()
    serializer_class = EstadoCompraListaSerializer

class EstadoPedidoListView(BaseListView):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoListaSerializer


class ProveedorListView(BaseListView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorListaSerializer


class CompraListView(BaseListView):
    queryset = Compra.objects.all()
    serializer_class = CompraListaSerializer

class PedidoListView(BaseListView):
    queryset = Pedido.objects.select_related('producto', 'proveedor').all()
    serializer_class = PedidoListaSerializer


class PedidoRequeridoListView(BaseListView):
    queryset = Pedido.objects.select_related('producto', 'proveedor').filter(estado=1).exclude(state=2) #para enviar nombre del producto y nombre de proveedor
    serializer_class = PedidoListaSerializer # en el selializer estan incluidos los campos dichos


class PedidoSolicitadoListView(BaseListView):
    queryset = Pedido.objects.select_related('producto', 'proveedor').filter(estado=2).exclude(state=2) #para enviar nombre del producto y nombre de proveedor
    serializer_class = PedidoSolicitadoListaSerializer # en el selializer estan incluidos los campos dichos

class PedidoProveedorconRequeridoListView(BaseListView):
    queryset = Pedido.objects.select_related('producto', 'proveedor').filter(estado=1)
    serializer_class = PedidoListaSerializer

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

class EstadoPedidoDetailView(RetrieveAPIView):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoDetalleSerializer

class ProveedorDetailView(RetrieveAPIView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorDetalleSerializer

class CompraDetailView(RetrieveAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraDetalleSerializer

class PedidoDetailView(RetrieveAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoDetalleSerializer

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

class EstadoPedidoCreateUpdateView(BaseCreateUpdateView):
    queryset = EstadoPedido.objects.all()
    serializer_class = EstadoPedidoDetalleSerializer

class ProveedorCreateUpdateView(BaseCreateUpdateView):
    queryset = Proveedor.objects.all()
    serializer_class = ProveedorDetalleSerializer

class PagoCompraCreateUpdateView(BaseCreateUpdateView):
    queryset = PagoCompra.objects.all()
    serializer_class = PagoCompraDetalleSerializer

class CompraCreateUpdateView(BaseCreateUpdateView):
    queryset = Compra.objects.all()
    serializer_class = CompraDetalleSerializer

class PedidoCreateUpdateView(BaseCreateUpdateView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoDetalleSerializer

    # def perform_create(self, serializer):
    #     # Obtén el ID del producto desde los datos que se reciben en la solicitud
    #     producto_id = self.request.data.get('producto')
    #     costo = self.request.data.get('costo')

    #     # Verifica si el producto existe
    #     try:
    #         producto = Producto.objects.get(id=producto_id)
    #     except Producto.DoesNotExist:
    #         raise ValidationError("El producto con el ID proporcionado no existe.")

    #     # Obtén el costo del producto
    #     cantidad_solicitada = producto.cantidad_x_empaque
    #     valor_esperado = costo

    #     # Guarda el pedido con el costo del producto
    #     serializer.save(valor_esperado=valor_esperado, cantidad_solicitada=cantidad_solicitada)

class CompraDetalleCreateUpdateView(BaseCreateUpdateView):
    queryset = CompraDetalle.objects.all()
    serializer_class = CompraDetalleDetalleSerializer


########################################################################################
########  VISTAS GENÉRICAS PARA MARCAR COMO ELIMINADO CADA MODELO ######################
########################################################################################


class EstadoCompraDeleteView(BaseDeleteView):
    model = EstadoCompra
    serializer_class = EstadoCompraDetalleSerializer

class EstadoPedidoDeleteView(BaseDeleteView):
    model = EstadoPedido
    serializer_class = EstadoPedidoDetalleSerializer

class ProveedorDeleteView(BaseDeleteView):
    model = Proveedor
    serializer_class = ProveedorDetalleSerializer

class PagoCompraDeleteView(BaseDeleteView):
    model = PagoCompra
    serializer_class = PagoCompraDetalleSerializer

class CompraDeleteView(BaseDeleteView):
    model = Compra
    serializer_class = CompraDetalleSerializer

class PedidoDeleteView(BaseDeleteView):
    model = Pedido
    serializer_class = PedidoDetalleSerializer

class CompraDetalleDeleteView(BaseDeleteView):
    model = CompraDetalle
    serializer_class = CompraDetalleDetalleSerializer





class PedidoBulkView(generics.GenericAPIView):
    queryset = Pedido.objects.all()
    serializer_class = PedidoListaSerializer


    def post(self, request, *args, **kwargs):
        print("llegnado al post")
        pedidos_data = request.data if isinstance(request.data, list) else [request.data]
        resultados = []
        errores = []

        for pedido_data in pedidos_data:
            serializer = self.get_serializer(data=pedido_data)
            if serializer.is_valid():
                self.perform_create(serializer)
                resultados.append(serializer.data)
            else:
                errores.append(serializer.errors)

        if errores:
            return Response({'resultados': resultados, 'errores': errores}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'resultados': resultados}, status=status.HTTP_201_CREATED)

    def put(self, request, *args, **kwargs):
        logger.warning(f"Llegnado al post: {request.data}")

        pedidos_data = request.data if isinstance(request.data, list) else [request.data]
        resultados = []
        errores = []

        for pedido_data in pedidos_data:
            pedido_id = pedido_data.get('id', None)
            if not pedido_id:
                errores.append({'error': 'Falta el campo ID para actualizar el pedido.'})
                continue

            try:
                instance = self.get_queryset().get(id=pedido_id)
            except Pedido.DoesNotExist:
                errores.append({'error': f'No se encontró el pedido con id {pedido_id}.'})
                continue

            serializer = self.get_serializer(instance, data=pedido_data, partial=True)
            if serializer.is_valid():
                #verificar si estado es 1(requerido) y cambiarlo a 2 (solicitado)
                #logger.warning(f"Estado actual: {instance.estado_id}") 
                if instance.estado_id== 1: 
                    instance.estado_id = 2
                self.perform_update(serializer)
                resultados.append(serializer.data)
            else:
                errores.append(serializer.errors)

        if errores:
            return Response({'resultados': resultados, 'errores': errores}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'resultados': resultados}, status=status.HTTP_200_OK)

    def perform_create(self, serializer):
        user = "usuario1"  # O usar: self.request.user.username
        serializer.save(creater=user, updater=user)

    def perform_update(self, serializer):
        instance = serializer.instance
        instance.updater = 'Usuario'  # O usar: self.request.user.username
        serializer.save(updater=instance.updater)
