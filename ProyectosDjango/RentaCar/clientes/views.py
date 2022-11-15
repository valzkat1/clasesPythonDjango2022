from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from clientes.models import Clientes
from django.core.mail import send_mail


# REQUEST
# GET  POST
def index(request):
    return render(request,"clientes.html",{"mensaje":"Hola Clientes"})


#@csrf_exempt
def resultado(request):
    if request.POST['nombre']:
        clienteB = Clientes.objects.filter(nombre__icontains=request.POST['nombre'])
        # SELECT * FROM clientes WHERE nombre like '%nombrePOST%'
        
        return render(request,"respuesta.html",{"clientes":clienteB,"mensaje":"consultado por nombre"})
    else:
        return render(request,"respuesta.html",{"mensaje":"Es necesario el criterio de busqueda","clientes":[]})
    

def listaClientes(request):
    return render(request,"respuesta.html",{"clientes":Clientes.objects.filter()})    

def editarCliForm(request):    
    id_=request.GET['id']
    objClienteEditar=Clientes.objects.get(id=id_)    
    return render(request,"editarClientes.html",{"cliente":objClienteEditar})

def editarClienteGuardar(request):    
    objClient=Clientes(nombre=request.POST['nombre'],edad=request.POST['edad'],email=request.POST['email'],fechaNacimi=request.POST['fechaNacimi'],id=request.POST['id'])
    objClient.save()
    return render(request,"respuesta.html",{"clientes":Clientes.objects.filter()})

def crearClienteForm(request):
    return render(request,"crearClientes.html",{"mesanje":"OK"})

def crearClienteGuardar(request):
    objeClienteNew=Clientes(nombre=request.POST['nombre'],edad=request.POST['edad'],email=request.POST['email'],fechaNacimi=request.POST['fechaNacimi'])
    objeClienteNew.save()
    return render(request,"respuesta.html",{"clientes":Clientes.objects.filter()})


def contacto(request):
    if request.method=='POST':
        nombre=request.POST['nombre']
        email=request.POST['email']
        asunto=request.POST['asunto']
        mensaje=request.POST['mensaje']
        send_mail(asunto,mensaje,email,['valzkat12@gmail.com'],fail_silently=False)
        
        return render(request,"procesoExitoso.html")
    else:
        return render(request,"contacto.html")
