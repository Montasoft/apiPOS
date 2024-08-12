# urls.py

from django.urls import path

from apps.baseapp import views
from .views import BancoListView, BancoDetailView, BancoCreateUpdateView, BancoDeleteView, DepartamentoListView, DepartamentoDetailView, DepartamentoCreateUpdateView, DepartamentoDeleteView, CiudadListView, CiudadDetailView, CiudadCreateUpdateView, CiudadDeleteView, TipoDocumentoListView, TipoDocumentoDetailView, TipoDocumentoCreateUpdateView, TipoDocumentoDeleteView, FormaPagoListView, FormaPagoDetailView, FormaPagoCreateUpdateView, FormaPagoDeleteView, TipoCuentaBancariaListView, TipoCuentaBancariaDetailView, TipoCuentaBancariaCreateUpdateView, TipoCuentaBancariaDeleteView
urlpatterns = [

    path('precargar', views.precargar, name="precargar"),

    path('Bancos/', BancoListView.as_view(), name='BancoListView'),
    path('Banco/<int:pk>/', BancoDetailView.as_view(), name='BancoDetailView'),
    path('Banco/create/', BancoCreateUpdateView.as_view(), name='BancoCreateUpdateView'),
    path('Banco/update/<int:pk>', BancoCreateUpdateView.as_view(), name='BancoCreateUpdateView'),
    path('Banco/delete/', BancoDeleteView.as_view(), name='BancoDeleteView'),

    path('Departamentos/', DepartamentoListView.as_view(), name='DeparetamentoListView'),
    path('Departamento/<int:pk>/', DepartamentoDetailView.as_view(), name='DeparetamentoDetailView'),
    path('Departamento/create/', DepartamentoCreateUpdateView.as_view(), name='DeparetamentoCreateUpdateView'),
    path('Departamento/update/<int:pk>', DepartamentoCreateUpdateView.as_view(), name='DeparetamentoCreateUpdateView'),
    path('Departamento/delete/', DepartamentoDeleteView.as_view(), name='DepartamentoDeleteView'),

    path('Ciudades/', CiudadListView.as_view(), name='CiudadListView'),
    path('Ciudad/<int:pk>/', CiudadDetailView.as_view(), name='CiudadDetailView'),
    path('Ciudad/create/', CiudadCreateUpdateView.as_view(), name='CiudadCreateUpdateView'),
    path('Ciudad/update/<int:pk>', CiudadCreateUpdateView.as_view(), name='CiudadCreateUpdateView'),
    path('Ciudad/delete/', CiudadDeleteView.as_view(), name='CiudadDeleteView'),

    path('TipoDocumento/', TipoDocumentoListView.as_view(), name='TipoDocumentoListView'),
    path('TipoDocumento/<int:pk>/', TipoDocumentoDetailView.as_view(), name='TipoDocumentoDetailView'),
    path('TipoDocumento/create/', TipoDocumentoCreateUpdateView.as_view(), name='TipoDocumentoCreateUpdateView'),
    path('TipoDocumento/update/<int:pk>', TipoDocumentoCreateUpdateView.as_view(), name='TipoDocumentoCreateUpdateView'),
    path('TipoDocumento/delete/', TipoDocumentoDeleteView.as_view(), name='TipoDocumentoDeleteView'),

    path('FormaPago/', FormaPagoListView.as_view(), name='FormaPagoListView'),
    path('FormaPago/<int:pk>/', FormaPagoDetailView.as_view(), name='FormaPagoDetailView'),
    path('FormaPago/create/', FormaPagoCreateUpdateView.as_view(), name='FormaPagoCreateUpdateView'),
    path('FormaPago/update/<int:pk>', FormaPagoCreateUpdateView.as_view(), name='FormaPagoCreateUpdateView'),
    path('FormaPago/delete/', FormaPagoDeleteView.as_view(), name='FormaPagoDeleteView'),

    path('TipoCuentaBancaria/', TipoCuentaBancariaListView.as_view(), name='TipoCuentaBancariaListView'),
    path('TipoCuentaBancaria/<int:pk>/', TipoCuentaBancariaDetailView.as_view(), name='TipoCuentaBancariaDetailView'),
    path('TipoCuentaBancaria/create/', TipoCuentaBancariaCreateUpdateView.as_view(), name='TipoCuentaBancariaCreateUpdateView'),
    path('TipoCuentaBancaria/update/<int:pk>', TipoCuentaBancariaCreateUpdateView.as_view(), name='TipoCuentaBancariaCreateUpdateView'),
    path('TipoCuentaBancaria/delete/', TipoCuentaBancariaDeleteView.as_view(), name='TipoDocumentoDeleteView'),


]


