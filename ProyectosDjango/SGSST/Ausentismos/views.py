from django.shortcuts import render,redirect
from Ausentismos.forms import FormularioAusentismos,FormularioIncapacidades
from Ausentismos.models import ausentismo
def crearAusentismo(request):
    if request.method=='POST':
        MiFormulario=FormularioIncapacidades(request.POST)
       # MiFormulario.fields['totalEmpresa']='0'
       # MiFormulario.fields['totalArl']='0'
       # MiFormulario.fields['totalAFP']='0'
       # MiFormulario.fields['totalEPS']='0'
       # MiFormulario.fields['totalIncapacidad']='0'
        
        if MiFormulario.is_valid():
             MiFormulario.save()
             return redirect("listarInca")
        else:
             return render(request,"Ausentismos/formularios.html",{"tituloFormulario":"Registrar Incapacidad","actionFormulario":"/ausentismos/crear/","contenidoFormulario":MiFormulario})
    else:
        MiFormulario=FormularioIncapacidades()
        return render(request,"Ausentismos/formularios.html",{"tituloFormulario":"Registrar Incapacidad","actionFormulario":"/ausentismos/crear/","contenidoFormulario":MiFormulario})


def listarAusentismo(request):
    return render(request,"Ausentismos/listaE.html",{"tituloListado":"Lista de Incapacidades","lista":ausentismo.objects.filter()})

def editarAusentismo(request):
    if (request.method=='POST'):
        id_=request.POST['id']
        objIncapacidad=ausentismo.objects.get(id=id_)
        miFormulario=FormularioIncapacidades(request.POST,instance=objIncapacidad)
        if miFormulario.is_valid():
            miFormulario.save()
            return redirect("listarInca")
        else:
            return render(request,"Ausentismos/editar.html",{"tituloFormulario":"Editar Incapacidades","actionFormulario":"/ausentismos/editar/","contenidoFormulario":miFormulario,"id":id_})
        
    else:
        id_=request.GET['id']
        objIncapacidad=ausentismo.objects.get(id=id_)
        miFormulario=FormularioIncapacidades(instance=objIncapacidad)
        return render(request,"Ausentismos/editar.html",{"tituloFormulario":"Editar Incapacidades","actionFormulario":"/ausentismos/editar/","contenidoFormulario":miFormulario,"id":id_})