from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from clientes.models import Clientes

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

def editarCli(request):    
    id_=request.GET['id']
    objClienteEditar=Clientes.objects.get(id=id_)    
    return render(request,"editarClientes.html",{"cliente":objClienteEditar})

def editarCliente(request):
    
    return render(request,"respuesta.html",{"clientes":Clientes.objects.filter()})