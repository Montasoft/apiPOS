from django.utils import timezone
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from rest_framework import generics
from rest_framework import mixins
from rest_framework.generics import RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from .models import Banco, Departamento, Ciudad, TipoDocumento, FormaPago, TipoCuentaBancaria
from .serializers import BancoListaSerializer, BancoDetalleSerializer, DepartamentoListaSerializer, DepartamentoDetalleSerializer, CiudadListaSerializer, CiudadDetalleSerializer, TipoDocumentoListaSerializer,TipoDocumentoDetalleSerializer, FormaPagoListaSerializer, FormaPagoDetalleSerializer, TipoCuentaBancariaListaSerializer, TipoCuentaBancariaDetalleSerializer
from .precargar import cargaInicial                                                                                     


def precargar(request):
    # vista creada para crecargar datos iniciales a la base de datos
    print("Se ha inicializador de manera correcta")
    return ("Se ha inicializado de manera correctoa: ", cargaInicial() )

class BaseListView (generics.ListAPIView):
    pagination_class = LimitOffsetPagination
    pagination_class.page_size = 20

########################################################################################
########  VISTAS GENÉRICAS PARA lISTA DE CADA MODELO ################################
########################################################################################


class BancoListView(BaseListView):
    queryset = Banco.objects.all()
    serializer_class = BancoListaSerializer

class DepartamentoListView(BaseListView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoListaSerializer
    
class CiudadListView(BaseListView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadListaSerializer
    
class TipoDocumentoListView(BaseListView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoListaSerializer
    
class FormaPagoListView(BaseListView):
    queryset = FormaPago.objects.all()
    serializer_class = FormaPagoListaSerializer
    
class TipoCuentaBancariaListView(BaseListView):
    queryset = TipoCuentaBancaria.objects.all()
    serializer_class = TipoCuentaBancariaListaSerializer
    
########################################################################################
########  VISTAS GENÉRICAS PARA DETALLES DE CADA MODELO ################################
########################################################################################
 

class BancoDetailView(RetrieveAPIView):
    queryset = Banco.objects.all()
    serializer_class = BancoDetalleSerializer

class DepartamentoDetailView(RetrieveAPIView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoDetalleSerializer

class CiudadDetailView(RetrieveAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadDetalleSerializer

class TipoDocumentoDetailView(RetrieveAPIView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoDetalleSerializer

class FormaPagoDetailView(RetrieveAPIView):
    queryset = FormaPago.objects.all()
    serializer_class = FormaPagoDetalleSerializer

class TipoCuentaBancariaDetailView(RetrieveAPIView):
    queryset = TipoCuentaBancaria.objects.all()
    serializer_class = TipoCuentaBancariaDetalleSerializer


########################################################################################
########  VISTAS GENÉRICAS PARA CREAR O ACTUALIZAR CADA MODELO ################################
########################################################################################


class BaseCreateUpdateView(generics.RetrieveUpdateAPIView, generics.CreateAPIView):

    partial = True  # Permite actualizaciones parciales (PATCH)

    def perform_create(self, serializer):
        # Asignar el valor del campo 'updater' y 'creater' antes de guardar la instancia
        user = "usuario1"  
#        user = self.request.user.username  
        serializer.save(creater=user, updater=user)

 
    def perform_update(self, serializer):
        # Obtén la instancia del objeto a actualizar
        instance = serializer.instance
        
        # Modifica cualquier campo adicional que no provenga del formulario
        instance.updater = 'Usuario'
        
        # Guarda los cambios del serializador junto con el campo adicional
        serializer.save(updater=instance.updater)

        print(instance)
        print(serializer)
                                       
        
class BancoCreateUpdateView(BaseCreateUpdateView):
    queryset = Banco.objects.all()
    serializer_class = BancoDetalleSerializer

class DepartamentoCreateUpdateView(BaseCreateUpdateView):
    queryset = Departamento.objects.all()
    serializer_class = DepartamentoDetalleSerializer

class CiudadCreateUpdateView(BaseCreateUpdateView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadDetalleSerializer

class TipoDocumentoCreateUpdateView(BaseCreateUpdateView):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocumentoDetalleSerializer

class FormaPagoCreateUpdateView(BaseCreateUpdateView):
    queryset = FormaPago.objects.all()
    serializer_class = FormaPagoDetalleSerializer

class TipoCuentaBancariaCreateUpdateView(BaseCreateUpdateView):
    queryset = TipoCuentaBancaria.objects.all()
    serializer_class = TipoCuentaBancariaDetalleSerializer


########################################################################################
########  VISTAS GENÉRICAS PARA MARCAR COMO ELIMINADO CADA MODELO ################################
########################################################################################


class BaseDeleteView(APIView):

    def patch(self, request):
        try:
            instance_id = request.data.get('id')
            instance = self.model.objects.get(pk=instance_id)
        except self.model.DoesNotExist:
            return Response({"error": f"{self.model.__name__} no encontrado"}, status=status.HTTP_404_NOT_FOUND)

        # Marcar registro como eliminado
        instance.deleter = 'Usuario'
        instance.state = 2
        instance.deleted = timezone.now()
        instance.save()

        serializer = self.serializer_class(instance)
        return Response(serializer.data)

class BancoDeleteView(BaseDeleteView):
    model = Banco
    serializer_class = BancoDetalleSerializer

class DepartamentoDeleteView(BaseDeleteView):
    model = Departamento
    serializer_class = DepartamentoDetalleSerializer

class CiudadDeleteView(BaseDeleteView):
    model = Ciudad
    serializer_class = CiudadDetalleSerializer
    
class TipoDocumentoDeleteView(BaseDeleteView):
    model = TipoDocumento
    serializer_class = TipoDocumentoDetalleSerializer
    
class FormaPagoDeleteView(BaseDeleteView):
    model = FormaPago
    serializer_class = FormaPagoDetalleSerializer
    
class TipoCuentaBancariaDeleteView(BaseDeleteView):
    model = TipoCuentaBancaria
    serializer_class = TipoCuentaBancariaDetalleSerializer
    


