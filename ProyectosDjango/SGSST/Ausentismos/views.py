from django.shortcuts import render
from Ausentismos.forms import FormularioAusentismos

def crearAusentismo(request):
    miFormulario=FormularioAusentismos()
    return render(request,"comunes/formularios.html",{"tituloFormulario":"Registrar Incapacidad","actionFormulario":"crearAusentismo","contenidoFormulario":miFormulario.as_div()})
