from django.shortcuts import render
from Ausentismos.forms import FormularioAusentismos,FormularioIncapacidades

def crearAusentismo(request):
    miFormulario=FormularioIncapacidades()
    return render(request,"comunes/formularios.html",{"tituloFormulario":"Registrar Incapacidad","actionFormulario":"crearAusentismo","contenidoFormulario":miFormulario.as_div()})
