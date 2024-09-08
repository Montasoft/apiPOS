from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.db.models import Sum, FloatField, F
from django.urls import reverse
from django.contrib.auth.decorators import login_required, user_passes_test

from apps.baseapp.models import BaseModel, Tercero, FormaPago
from apps.inventario.models import Producto


#######################################################################################
'''
Se definen las clases:
    EstadoCompra
    Proveedor
    Compra
    CompraDetalles
    PagoCompra
'''

#######################################################################################
class EstadoPedido(BaseModel):
    '''
    1- requerido (recien creado el registro)
    2- solicitado (ya se ha pedido a un proveedor)
    3- recibido (pedido cumplido)
    4- rechazado (llegó pero no se recibió, se especifica la cuda)
    5-anulado (pasó el tiempo esperado y no se recició)

    '''
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('compras:EstadoPedidoDetailView', kwargs={'pk' :self.id})
    



#######################################################################################
class EstadoCompra(BaseModel):
    '''
    1 creada (antes de agregar detalles)
    2 abierta (con detalles agregados)
    3 recibida (sin pago o pago parcial)
    4 pagada
    5 anulada (debe tener valor = 0)

    '''
    nombre = models.CharField(max_length=25)
    descripcion = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('compras:EstadoCompraDetailView', kwargs={'pk' :self.id})
    


#######################################################################################
class Proveedor(Tercero):

    condiciones_credito = models.CharField(max_length=256, null=True, blank=True)
    condiciones_descuento = models.CharField(max_length=256, null=True, blank=True)

    class Meta:
        ordering =['nombre']

    def __str__(self):
        return  self.nombre

    def get_absolute_url(self):
        return reverse('compras:ProveedorDetailView', kwargs={'pk' :self.id})




#######################################################################################
class Pedido(BaseModel):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    estado = models.ForeignKey(EstadoPedido, on_delete=models.CASCADE, default=1)
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    cantidad_solicitada = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_solicitud = models.DateField()
    fecha_esperado = models.DateField()
    valor_esperado = models.DecimalField(max_digits=10, decimal_places=2)
    fecha_recibido = models.DateField()
    cantidad_recibida = models.DecimalField(max_digits=10, decimal_places=2)
    valor_recibido = models.DecimalField(max_digits=10, decimal_places=2)
    recibido_por = models.CharField(max_length=30, null=True, blank= True)
    nota = models.CharField(max_length= 250, null=True, blank= True)
    
    class Meta:
        ordering =['id']
        verbose_name = "Pedido"
        verbose_name_plural = "Pedidos"

    def __str__(self):
        return  str(self.id)
    
    def get_absolute_url(self):
        return reverse('compras:PedidoDetailView', kwargs={'pk' :self.id})



#######################################################################################
class Compra(BaseModel):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    fecha_compra = models.DateField()
    num_factura_proveedor = models.CharField(max_length=30, null=True, blank= True)
    valor_compra = models.DecimalField(max_digits=10, decimal_places=2)
    forma_pago = models.ForeignKey (FormaPago, on_delete=models.CASCADE, default =1)
    fecha_vence = models.DateField()
    fecha_recibido = models.DateField()
    nota = models.CharField(max_length= 250, null=True, blank= True)
    estado = models.ForeignKey(EstadoCompra, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering =['id']
        verbose_name = "Compra"
        verbose_name_plural = "Compras"

    def __str__(self):
        return  str(self.id)
    
    def get_absolute_url(self):
        return reverse('compras:CompraDetailView', kwargs={'pk' :self.id})


    @property
    def total(self): 
 
        # Aplica un filtro para seleccionar solo los registros con estado igual 0 no borrados
        detalleCompraNoBorrado = self.compradetalles_set.filter(state=0)
        
        return detalleCompraNoBorrado.aggregate(
           total=Sum(F('paquetes')*F('unidades')* F('neto'), output_field=FloatField())
        )['total']



#######################################################################################
class CompraDetalle(BaseModel):
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    paquetes = models.DecimalField(max_digits=10, decimal_places=2)
    unidades = models.IntegerField(default=1)
    valor_paquete = models.FloatField()
    descuento_pre_iva = models.FloatField(default =0, verbose_name='Desc pre')
    descuento_pos_iva = models.FloatField(default =0, verbose_name='Desc pos')
    iva = models.IntegerField (default=0)
    flete = models.DecimalField(max_digits=6, decimal_places=4, default =0 )
    neto = models.DecimalField(max_digits=10, decimal_places=2)
    observacion = models.CharField(max_length=250, null=True, blank= True)
    
    @property
    def cantidad(self):
        return self.paquetes * self.unidades
        
    class Meta:
        ordering =['id']
        verbose_name = "CompraDetalle"
        verbose_name_plural = "CompraDetalles"
   
    def __str__(self):  
        cantidad =self.paquetes*self.unidades
        return f'({cantidad}) unidades de {self.producto.nombre}'
    
    def get_absolute_url(self):
        return reverse('compras:CompraDetalleDetailView', kwargs={'pk' :self.id})



 #######################################################################################
class PagoCompra(BaseModel):
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE)
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    fecha_pago = models.DateField()
    forma_pago =  models.ForeignKey(FormaPago, on_delete=models.CASCADE)
    valor_pago = models.FloatField()
    cajero = models.ForeignKey(User, on_delete=models.CASCADE)
    nota = models.CharField(max_length= 250, null=True, blank= True  )
    
    class Meta:
        ordering =['id']
        verbose_name = "pagoCompra"
        verbose_name_plural = "PagosCompra"

    def __str__(self):
        return  str(self.valor_pago)

    def get_absolute_url(self):
        return reverse('compras:PagoCompraDetailView', kwargs={'pk' :self.id})
    
