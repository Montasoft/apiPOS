# serializers.py

from rest_framework import serializers
from .models import Categoria, SubCategoria, EstadoProducto, Producto


####################################################################
#lista de Categoria
class CategoriaListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
   #     fields = '__all__'
        fields = 'id', 'nombre', 'descripcion', 'get_absolute_url'

#detalle de cada Categoria
class CategoriaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
   
        fields = 'id', 'nombre', 'descripcion', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',
#


####################################################################
#lista de SubCategoriaes
class SubCategoriaListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
   #     fields = '__all__'
        fields = 'id', 'nombre', 'descripcion', 'categoria', 'get_absolute_url'

#detalle de cada SubCategoria
class SubCategoriaDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategoria
   
        fields = 'id', 'nombre', 'descripcion', 'categoria', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',
#



####################################################################
#lista de EstadoProductos
class EstadoProductoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoProducto
   #     fields = '__all__'
        fields = 'id', 'nombre', 'descripcion', 'get_absolute_url'

#detalle de cada EstadoProducto
class EstadoProductoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = EstadoProducto
   
        fields =  'id', 'nombre', 'descripcion', 'get_absolute_url' ,'state', 'created','creater','updated','updater','deleted','deleter',



####################################################################
#lista de Productos
class ProductoListaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
   #     fields = '__all__'
        fields = 'id', 'nombre', 'costo', 'precio_venta', 'existencias', 'get_absolute_url'

#detalle de cada Producto
class ProductoDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
   
        fields = 'id', 'nombre', 'codigo_barras', 'categoria', 'subcategoria', 'costo', 'precio_venta', 'precio_mayor', 'iva', 'existencias', 'estado', 'dim_Alto', 'dim_Ancho', 'dim_fondo', 'peso', 'Nota', 'descripcion', 'cantidad_x_empaque', 'imagen', 'get_absolute_url','state', 'created','creater','updated','updater','deleted','deleter',

