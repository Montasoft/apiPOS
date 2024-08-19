# urls.py

from django.urls import path
from .views import CompraCreateUpdateView, CompraDeleteView, CompraDetailView, CompraDetalleCreateUpdateView, CompraDetalleDeleteView, CompraDetalleDetailView, EstadoCompraCreateUpdateView, EstadoCompraDeleteView, EstadoCompraDetailView, EstadoCompraListView, PagoCompraCreateUpdateView, PagoCompraDeleteView, PagoCompraDetailView, ProveedorListView, CompraListView, CompraDetalleListView, PagoCompraListView, ProveedorDetailView, ProveedorCreateUpdateView, ProveedorDeleteView

app_name = 'compras'

urlpatterns = [
 
    path('EstadoCompra/', EstadoCompraListView.as_view(), name='EstadoCompraListView'),
    path('EstadoCompra/<int:pk>/', EstadoCompraDetailView.as_view(), name='EstadoCompraDetailView'),
    path('EstadoCompra/create/', EstadoCompraCreateUpdateView.as_view(), name='EstadoCompraCreateUpdateView'),
    path('EstadoCompra/update/<int:pk>', EstadoCompraCreateUpdateView.as_view(), name='EstadoCompraCreateUpdateView'),
    path('EstadoCompra/delete/', EstadoCompraDeleteView.as_view(), name='EstadoCompraDeleteView'),

    path('Proveedor/', ProveedorListView.as_view(), name='ProveedorListView'),
    path('Proveedor/<int:pk>/', ProveedorDetailView.as_view(), name='ProveedorDetailView'),
    path('Proveedor/create/', ProveedorCreateUpdateView.as_view(), name='ProveedorCreateUpdateView'),
    path('Proveedor/update/<int:pk>', ProveedorCreateUpdateView.as_view(), name='ProveedorCreateUpdateView'),
    path('Proveedor/delete/', ProveedorDeleteView.as_view(), name='ProveedorDeleteView'),

    path('Compras/', CompraListView.as_view(), name='CompraListView'),
    path('Compra/<int:pk>/', CompraDetailView.as_view(), name='CompraDetailView'),
    path('Compra/create/', CompraCreateUpdateView.as_view(), name='CompraCreateUpdateView'),
    path('Compra/update/<int:pk>', CompraCreateUpdateView.as_view(), name='CompraCreateUpdateView'),
    path('Compra/delete/', CompraDeleteView.as_view(), name='CompraDeleteView'),

    path('CompraDetalle/', CompraDetalleListView.as_view(), name='CompraDetalleListView'),
    path('CompraDetalle/<int:pk>/', CompraDetalleDetailView.as_view(), name='CompraDetalleDetailView'),
    path('CompraDetalle/create/', CompraDetalleCreateUpdateView.as_view(), name='CompraDetalleCreateUpdateView'),
    path('CompraDetalle/update/<int:pk>', CompraDetalleCreateUpdateView.as_view(), name='CompraDetalleCreateUpdateView'),
    path('CompraDetalle/delete/', CompraDetalleDeleteView.as_view(), name='CompraDetalleDeleteView'),

    path('PagoCompra/', PagoCompraListView.as_view(), name='PagoCompraListView'),
    path('PagoCompra/<int:pk>/', PagoCompraDetailView.as_view(), name='PagoCompraDetailView'),
    path('PagoCompra/create/', PagoCompraCreateUpdateView.as_view(), name='PagoCompraCreateUpdateView'),
    path('PagoCompra/update/<int:pk>', PagoCompraCreateUpdateView.as_view(), name='PagoCompraCreateUpdateView'),
    path('PagoCompra/delete/', PagoCompraDeleteView.as_view(), name='PagoCompraDeleteView'),

    path('', EstadoCompraListView.as_view(), name='EstadoCompraListView'),

]



