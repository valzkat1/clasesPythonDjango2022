from django.shortcuts import render

# REQUEST
# GET  POST
def index(request):
    return render(request,"clientes.html",{"mensaje":"Hola Clientes"})


def resultado(request):
    return render(request,"respuesta.html",{"nombre":request.GET['nombre'],"edad":request.GET['edad']})