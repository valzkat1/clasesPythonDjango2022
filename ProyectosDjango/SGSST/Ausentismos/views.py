from django.shortcuts import render,redirect
from Ausentismos.forms import FormularioAusentismos,FormularioIncapacidades
from Ausentismos.models import ausentismo
def crearAusentismo(request):
    if request.method=='POST':
        MiFormulario=FormularioIncapacidades(request)
        MiFormulario.fields['totalEmpresa']='0'
        MiFormulario.fields['totalArl']='0'
        MiFormulario.fields['totalAFP']='0'
        MiFormulario.fields['totalEPS']='0'
        MiFormulario.fields['totalIncapacidad']='0'
        
        if MiFormulario.is_valid():
             MiFormulario.save()
             return redirect("listarInca")
    else:
        miFormulario=FormularioIncapacidades()
        return render(request,"comunes/formularios.html",{"tituloFormulario":"Registrar Incapacidad","actionFormulario":"/ausentismos/crear/","contenidoFormulario":miFormulario.as_div()})


def listarAusentismo(request):
    return render(request,"Ausentismos/listarE.html",{"tituloListado":"Lista de Incapacidades","lista":ausentismo.objects.filter()})