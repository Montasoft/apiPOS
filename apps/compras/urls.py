# urls.py

from django.urls import path
from .views import EstadoCompraListView, ProveedorListView, CompraListView, CompraDetalleListView, PagoCompraListView, ProveedorDetailView



app_name = 'compras'

urlpatterns = [
 
    path('EstadoCompra/', EstadoCompraListView.as_view(), name='EstadoCompraListView'),
 #   path('Banco/<int:pk>/', BancoDetailView.as_view(), name='BancoDetailView'),
  #  path('Banco/create/', BancoCreateUpdateView.as_view(), name='BancoCreateUpdateView'),
   # path('Banco/update/<int:pk>', BancoCreateUpdateView.as_view(), name='BancoCreateUpdateView'),
    #path('Banco/delete/', BancoDeleteView.as_view(), name='BancoDeleteView'),

    path('Proveedor/', ProveedorListView.as_view(), name='ProveedorListView'),
    path('Proveedor/<int:pk>/', ProveedorDetailView.as_view(), name='ProveedorDetailView'),

    path('Compras/', CompraListView.as_view(), name='CompraListView'),
    path('CompraDetalle/', CompraDetalleListView.as_view(), name='CompraDetalleListView'),
    path('PagoCompraListView/', PagoCompraListView.as_view(), name='PagoCompraListView'),
 
    path('', EstadoCompraListView.as_view(), name='EstadoCompraListView'),

]



