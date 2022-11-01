from django.contrib import admin
from clientes.models import Clientes
from clientes.models import Venta
from clientes.models import Tipos

admin.site.register(Clientes)
admin.site.register(Venta)
admin.site.register(Tipos)
