from django.shortcuts import render,redirect
from Usuarios.forms import FormularioUsuarios,FormularioUser
from Usuarios.models import usuario

def crearUsuarios(request):
    if request.method=='POST':
        print('aca se recibe formulario')
        miFormulario=FormularioUser(request.POST)
        if(miFormulario.is_valid()):
            miFormulario.save()
            return redirect('listaUsu')
    else:             
        miFormularioUsuarios=FormularioUser()
        return render(request,"comunes/formularios.html",{"actionFomulario":"crearUsuario","contenidoFormulario":miFormularioUsuarios.as_div(),"tituloFormulario":"Crear Usuarios"})
    
    
def listarUsuarios(request):
    return render(request,'Usuarios/listarU.html',{"tituloListado":"Lista de Usuarios","lista":usuario.objects.filter()})    
    


