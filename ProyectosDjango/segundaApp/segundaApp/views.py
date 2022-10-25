
from django.http import HttpResponse
from django.template import loader


def index(request):
    plantilla=loader.get_template('index.html')    
    pagina=plantilla.render({'mensaje':'Cualquier dato a enviar a la plantilla'})
    return HttpResponse(pagina)

def nosotros(request):
    plantilla=loader.get_template('nosotros.html')    
    pagina=plantilla.render({'mensaje':'Cualquier dato a enviar a la plantilla'})
    return HttpResponse(pagina)