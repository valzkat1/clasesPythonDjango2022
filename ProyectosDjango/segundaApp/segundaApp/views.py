
from django.http import HttpResponse
from django.template import loader

from segundaApp.persona import persona
from django.shortcuts import render



def index(request):
    plantilla=loader.get_template('index.html')    
    pagina=plantilla.render({'mensaje':'Cualquier dato a enviar a la plantilla  --  '})
    return HttpResponse(pagina)

def nosotros(request):
    plantilla=loader.get_template('nosotros.html')    
    pagina=plantilla.render({'mensaje':'Cualquier dato a enviar a la plantilla'})
    return HttpResponse(pagina)


def recorrerLista(request):
    perso1=persona("Pepe",20)
    perso2=persona("Victor",30)
    perso3=persona("Carlos",12)
    listaPersonas=[]
    listaPersonas.append(perso1)
    listaPersonas.append(perso2)
    listaPersonas.append(perso3)
    listaPersonas.append(persona("Maria",22))
    return render(request,"listado.html",{"listap":listaPersonas})

def conHerencia(request):
    return render(request,"plantillahija.html",{"data":"OK"})


def segundaHija(request):
    return render(request,"hija2.html",{"data":"ok"})


