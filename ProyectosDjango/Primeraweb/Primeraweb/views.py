from django.http import HttpResponse

def index(request):   
    return HttpResponse("Hola mundo Django <br/> <a href='../paginasaludo/Victor'>Ir al saludo</a>")


def saludo(request,nombre):
    return HttpResponse("<div style='color:red'>Bienvenid@ "+nombre+" </div><br/> <a href='../paginadespedida/30'>Ir a la despedida</a>")


def despedida(request,edad):
    return HttpResponse("<div style='color:blue;'> La edad es: "+str(edad)+"  </div>")