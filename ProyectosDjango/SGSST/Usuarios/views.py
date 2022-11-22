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
    

def edicionUsuarios(request):
    if request.method=='POST':
        id_=request.POST['id']
        UsuarioEditado=usuario.objects.get(id=id_) 
        miFormulario=FormularioUser(request.POST,instance=UsuarioEditado)
        if miFormulario.is_valid():
            miFormulario.save()            
            return redirect("listaUsu")
    else:  
        id_=request.GET['id']
        UsuarioEditado=usuario.objects.get(id=id_) 
        miFormulario=FormularioUser(instance=UsuarioEditado) 
        contexto={"tituloFomulario":"Editar Clientes","actionFormulario":"/usuarios/editar/","contenidoFormulario":miFormulario.as_div(),"id":id_}
        return render(request,"comunes/formulariosE.html",contexto)


def eliminarUsuario(request):
    id_=request.GET['id']
    usuarioEliminar= usuario.objects.get(id=id_)
    usuarioEliminar.delete()
    return redirect("listaUsu")