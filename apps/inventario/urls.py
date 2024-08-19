# urls.py

from django.urls import path
from .views import CategoriaCreateUpdateView, CategoriaDeleteView, CategoriaDetailView, CategoriaListView, EstadoProductoCreateUpdateView, EstadoProductoDeleteView, EstadoProductoDetailView, EstadoProductoListView, ProductoCreateUpdateView, ProductoDeleteView, ProductoDetailView, ProductoListView, SubCategoriaCreateUpdateView, SubCategoriaDeleteView, SubCategoriaDetailView, SubCategoriaListView

app_name = 'inventario'

urlpatterns = [
 
    path('Categoria/', CategoriaListView.as_view(), name='CategoriaListView'),
    path('Categoria/<int:pk>/', CategoriaDetailView.as_view(), name='CategoriaDetailView'),
    path('Categoria/create/', CategoriaCreateUpdateView.as_view(), name='CategoriaCreateUpdateView'),
    path('Categoria/update/<int:pk>', CategoriaCreateUpdateView.as_view(), name='CategoriaCreateUpdateView'),
    path('Categoria/delete/', CategoriaDeleteView.as_view(), name='CategoriaDeleteView'),

    path('SubCategoria/', SubCategoriaListView.as_view(), name='SubCategoriaListView'),
    path('SubCategoria/<int:pk>/', SubCategoriaDetailView.as_view(), name='SubCategoriaDetailView'),
    path('SubCategoria/create/', SubCategoriaCreateUpdateView.as_view(), name='SubCategoriaCreateUpdateView'),
    path('SubCategoria/update/<int:pk>', SubCategoriaCreateUpdateView.as_view(), name='SubCategoriaCreateUpdateView'),
    path('SubCategoria/delete/', SubCategoriaDeleteView.as_view(), name='SubCategoriaDeleteView'),

    path('EstadoProducto/', EstadoProductoListView.as_view(), name='EstadoProductoListView'),
    path('EstadoProducto/<int:pk>/', EstadoProductoDetailView.as_view(), name='EstadoProductoDetailView'),
    path('EstadoProducto/create/', EstadoProductoCreateUpdateView.as_view(), name='EstadoProductoCreateUpdateView'),
    path('EstadoProducto/update/<int:pk>', EstadoProductoCreateUpdateView.as_view(), name='EstadoProductoCreateUpdateView'),
    path('EstadoProducto/delete/', EstadoProductoDeleteView.as_view(), name='EstadoCompraDeleteView'),

    path('Producto/', ProductoListView.as_view(), name='ProductoListView'),
    path('Producto/<int:pk>/', ProductoDetailView.as_view(), name='ProductoDetailView'),
    path('Producto/create/', ProductoCreateUpdateView.as_view(), name='ProductoCreateUpdateView'),
    path('Producto/update/<int:pk>', ProductoCreateUpdateView.as_view(), name='ProductoCreateUpdateView'),
    path('Producto/delete/', ProductoDeleteView.as_view(), name='ProductoDeleteView'),

    path('', ProductoListView.as_view(), name='ProductoListView'),

]



