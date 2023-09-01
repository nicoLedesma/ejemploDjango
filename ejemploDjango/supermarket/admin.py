from pydoc import cli
from django.contrib import admin
from supermarket.models import Client, Venta, Producto


class VentaAdmin(admin.ModelAdmin):
    def get_venta_cliente_last_name(self, obj):
        return obj.cliente.last_name
    get_venta_cliente_last_name.short_description = 'Apellido'

    def get_cliente_es_socio(self, obj):
        return obj.cliente.socio
    get_cliente_es_socio.short_description = "es socio"

    search_fields = ('date','cliente__name', 'cliente__socio_number', 'cliente__last_name')
    list_display = ('id', 'date', 'get_venta_cliente_last_name', 'get_cliente_es_socio', 'total_ammount')
    list_display_links = ('id', 'get_venta_cliente_last_name')

# Register your models here.
admin.site.register(Client)
admin.site.register(Venta, VentaAdmin)
admin.site.register(Producto)