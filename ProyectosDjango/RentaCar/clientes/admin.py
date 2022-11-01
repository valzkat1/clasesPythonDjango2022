from django.contrib import admin
from clientes.models import Clientes
from clientes.models import Venta
from clientes.models import Tipos

class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre","edad","email","fechaNacimi")
    search_fields=("nombre","email","edad")

admin.site.register(Clientes, ClientesAdmin)

class AdminitradorVentas(admin.ModelAdmin):
    list_display=("fecha","total","cliente")
    search_fields=("cliente","fecha")

admin.site.register(Venta,AdminitradorVentas)


class AdminitradorTipos(admin.ModelAdmin):
    list_display=("nombre","descripcion")
    search_fields=("nombre","descripcion")
    
admin.site.register(Tipos,AdminitradorTipos)
