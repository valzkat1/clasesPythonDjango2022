from django.shortcuts import render
from Usuarios.forms import FormularioUsuarios,FormularioUser

def crearUsuarios(request):
    if request.method=='POST':
        print('aca se recibe formulario')
        miFormulario=FormularioUser(request.POST)
        if(miFormulario.is_valid()):
            miFormulario.save()
        
    else:             
        miFormularioUsuarios=FormularioUser()
        return render(request,"comunes/formularios.html",{"actionFomulario":"crearUsuario","contenidoFormulario":miFormularioUsuarios.as_div(),"tituloFormulario":"Crear Usuarios"})


