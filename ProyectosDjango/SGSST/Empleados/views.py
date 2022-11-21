from django.shortcuts import render
from Empleados.forms import FormularioEmpleados
from Empleados.models import empleado

def crearEmpleado(request):
    if request.method=='POST':
        MiFormu=FormularioEmpleados()
        
    else:
        miFormulario=FormularioEmpleados()
        return render(request,"comunes/formularios.html",{"tituloFormulario":"Crear Empleado","actionFormulario":"crearEmpleado","contenidoFormulario":miFormulario.as_div()})


def listarEmpleados(request):
    return render(request,'Empleados/listaE.html',{"tituloListado":"Lista de Empleados","lista":empleado.objects.filter()})
    
