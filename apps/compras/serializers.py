# serializers.py

from rest_framework import serializers
from .models import Compra, CompraDetalle, EstadoCompra , PagoCompra, Proveedor

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
   
        fields = 'id', 'producto', 'cantidad', 'neto', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',



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

