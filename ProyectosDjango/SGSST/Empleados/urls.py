from django.urls import path
from Empleados import views

urlpatterns = [
    
    path('crear/',views.crearEmpleado),
    path('listar/',views.listarEmpleados)
    
]

