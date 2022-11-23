from django.shortcuts import render,redirect
from Empleados.forms import FormularioEmpleados,FormularioEmp
from Empleados.models import empleado

def crearEmpleado(request):
    if request.method=='POST':
        MiFormu=FormularioEmp(request.POST)
        if MiFormu.is_valid():
            MiFormu.save()
            return redirect("listarEmp")
    else:
        miFormulario=FormularioEmp()
        return render(request,"comunes/formularios.html",{"tituloFormulario":"Crear Empleado","actionFormulario":"/empleados/crear/","contenidoFormulario":miFormulario.as_div()})


def listarEmpleados(request):
    return render(request,'Empleados/listaE.html',{"tituloListado":"Lista de Empleados","lista":empleado.objects.filter()})
    

def editarEmpleados(request):
    if(request.method=='POST'):
        id_=request.POST['id']
        EmpleadoEdicion=empleado.objects.get(id=id_)
        miFormulario=FormularioEmp(request.POST,instance=EmpleadoEdicion)
        if miFormulario.is_valid():
            miFormulario.save()
            return redirect("listarEmp")
        
    else:
        id_=request.GET['id']
        EmpleadoEditado = empleado.objects.get(id=id_)
        miFormulario = FormularioEmp(instance=EmpleadoEditado)
        return render(request,"comunes/formulariosE.html",{"tituloFormulario":"Editar Empleados","actionFormulario":"/empleados/editar/","contenidoFormulario":miFormulario.as_div(),"id":id_})     
    
def eliminarEmpleado(request):
    id_=request.GET['id']
    objetoEliminar=empleado.objects.get(id=id_)
    objetoEliminar.delete()
    return redirect("listarEmp")