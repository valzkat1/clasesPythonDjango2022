from django.shortcuts import render
from Usuarios.forms import FormularioUsuarios

def crearUsuarios(request):    
    miFormularioUsuarios=FormularioUsuarios()
    return render(request,"comunes/formularios.html",{"actionFomulario":"crearUsuario","contenidoFormulario":miFormularioUsuarios.as_div(),"tituloFormulario":"Crear Usuarios"})
