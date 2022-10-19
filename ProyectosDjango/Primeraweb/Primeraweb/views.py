from django.http import HttpResponse
from django.template import Template,Context,loader

from Primeraweb.persona import persona

def index(request):   
    return HttpResponse("Hola mundo Django <br/> <a href='../paginasaludo/Victor'>Ir al saludo</a>")


def saludo(request,nombre):
    return HttpResponse("<div style='color:red'>Bienvenid@ "+nombre+" </div><br/> <a href='../paginadespedida/30'>Ir a la despedida</a>")


def despedida(request,edad):
    return HttpResponse("<div style='color:blue;'> La edad es: "+str(edad)+"  </div>")


def paginaplantilla(request,nombre):
    vista=open('E:/BVC/reposa2censo/clasesPythonDjango2022/ProyectosDjango/Primeraweb/Primeraweb/plantillas/index.html')
    plantilla=Template(vista.read())
    vista.close()
    contexto = Context({'nombre':nombre})
    cadenaHttpResponse = plantilla.render(contexto)
    return HttpResponse(cadenaHttpResponse)

def paginaPlantillaLoader(request):
    
    perso=persona('Pepe',40)
    
    vista=loader.get_template('index.html')
    cadenaResponse=vista.render({'nombre':'Pepe','persona':perso})
    return HttpResponse(cadenaResponse)





## M V C
## M T V