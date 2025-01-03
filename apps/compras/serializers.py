# serializers.py

from rest_framework import serializers
from .models import Compra, CompraDetalle, EstadoCompra , PagoCompra, Proveedor, EstadoPedido, Pedido

####################################################################
#lista de EstadoCompra
class EstadoCompraListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCompra
   #     fields = '__all__'
        fields = 'id', 'nombre', 'descripcion', 'get_absolute_url'

#detalle de cada EstadoCompra
class EstadoCompraDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoCompra
   
        fields = 'id', 'nombre', 'descripcion', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',
#


####################################################################
#lista de EstadoPedido
class EstadoPedidoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
   #     fields = '__all__'
        fields = 'id', 'nombre', 'descripcion', 'get_absolute_url'

#detalle de cada EstadoPedido
class EstadoPedidoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoPedido
   
        fields = 'id', 'nombre', 'descripcion', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',
#



####################################################################
#lista de Proveedores
class ProveedorListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
   #     fields = '__all__'
        fields = 'id', 'nombre', 'whatsapp', 'get_absolute_url'

#detalle de cada Proveedor
class ProveedorDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proveedor
   
        fields = 'id', 'nombre', 'tipo_documento', 'numero_documento',  'ciudad',  'direccion',  'barrio',  'ubicacion_GPS',  'telefono',  'whatsapp',  'email', 'condiciones_credito', 'condiciones_descuento', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',
#



####################################################################
#lista de Compras
class CompraListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
   #     fields = '__all__'
        fields = 'id', 'fecha_compra', 'proveedor', 'valor_compra', 'get_absolute_url'

#detalle de cada Compra
class CompraDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
   
        fields = 'id', 'fecha_compra', 'proveedor', 'valor_compra', 'num_factura_proveedor', 'forma_pago', 'fecha_vence', 'fecha_recibido', 'nota', 'estado', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',


####################################################################
#lista de Pedidos
class PedidoListaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    proveedor_nombre = serializers.CharField(source='proveedor.nombre', read_only=True)
    producto_costo = serializers.CharField(source='producto.costo', read_only=True)
    producto_cantidad_x_empaque = serializers.CharField(source='producto.cantidad_x_empaque', read_only=True)

    class Meta:         
        model = Pedido
   #     fields = '__all__'
        fields = 'id', 'producto', 'producto_nombre',  'producto_costo', 'producto_cantidad_x_empaque', 'estado', 'proveedor', 'proveedor_nombre', 'cantidad_solicitada', 'valor_esperado', 'cantidad_recibida', 'valor_recibido', 'get_absolute_url'

#lista de Pedidos en estado solicitado
class PedidoSolicitadoListaSerializer(serializers.ModelSerializer):
    producto_nombre = serializers.CharField(source='producto.nombre', read_only=True)
    proveedor_nombre = serializers.CharField(source='proveedor.nombre', read_only=True)


    class Meta:         
        model = Pedido
   #     fields = '__all__'
        fields = 'id', 'producto', 'producto_nombre', 'estado', 'proveedor', 'proveedor_nombre', 'cantidad_solicitada', 'valor_esperado', 'cantidad_recibida', 'valor_recibido', 'recibido_por', 'nota', 'get_absolute_url'


#detalle de cada Pedido
class PedidoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
   
        fields = 'id', 'producto', 'estado', 'proveedor', 'cantidad_solicitada', 'fecha_solicitud', 'fecha_esperado', 'valor_esperado', 'fecha_recibido', 'cantidad_recibida', 'valor_recibido', 'recibido_por', 'nota', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',



####################################################################
#lista de CompraDetalles
class CompraDetalleListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraDetalle
   #     fields = '__all__'
        fields = 'id', 'producto', 'cantidad', 'neto', 'get_absolute_url'

#detalle de cada CompraDetalle
class CompraDetalleDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompraDetalle
   
        fields = 'id', 'compra', 'producto', 'paquetes', 'unidades', 'valor_paquete', 'descuento_pre_iva', 'descuento_pos_iva', 'iva', 'flete', 'neto', 'observacion', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',


####################################################################
#lista de PagoCompras
class PagoCompraListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoCompra
   #     fields = '__all__'
        fields = 'id', 'compra', 'fecha_pago', 'valor', 'get_absolute_url'

#detalle de cada PagoCompra
class PagoCompraDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = PagoCompra
   
        fields = 'id', 'proveedor', 'compra', 'fecha_pago', 'forma_pago', 'valor_pago', 'cajero', 'nota', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',

