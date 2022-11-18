from django.shortcuts import render
from Empleados.forms import FormularioEmpleados

def crearEmpleado(request):
    miFormulario=FormularioEmpleados()
    return render(request,"comunes/formularios.html",{"tituloFormulario":"Crear Empleado","actionFormulario":"crearEmpleado","contenidoFormulario":miFormulario.as_div()})
