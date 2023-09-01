from tokenize import blank_re
from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True)
    email = models.EmailField(null=True)
    cuit = models.CharField(max_length=15, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    fec_nac = models.DateField(null=True)
    socio = models.BooleanField(default=True)
    socio_number = models.IntegerField(null=True)

    def __str__(self):
        return f'{self.name}, {self.last_name}'
    
class Venta(models.Model):
    cliente = models.ForeignKey('Client', on_delete=models.CASCADE,)
    total_ammount = models.DecimalField('Monto total', decimal_places=2, max_digits=8, null=True, blank=True)
    date = models.DateField('Fecha de la compra', blank=False)

    def __str__(self):
        return f'{self.cliente} gasto {self.total_ammount} el dia {self.date}'
    
    def calcular_total(self):
        detalles = Detalle.objects.filter(venta=self)
        # suma = 0
        # for detalle in detalles:
        #     producto = detalle.producto
        #     precio = producto.precio
        #     cantidad = detalle.cantidad
        #     sum += precio * cantidad
        suma = sum(detalle.producto.precio * detalle.cantidad for detalle in detalles)
        self.total_ammount = suma
        self.save()

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(decimal_places=2, max_digits=8 )
    
    def __str__(self) -> str:
        return self.nombre

class Detalle(models.Model):
    venta = models.ForeignKey('Venta', related_name='detalle', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    producto = models.ForeignKey("Producto",on_delete=models.CASCADE)