from django.shortcuts import render,redirect
from Ausentismos.forms import FormularioAusentismos,FormularioIncapacidades
from Ausentismos.models import ausentismo
def crearAusentismo(request):
    if request.method=='POST':
        MiFormulario=FormularioIncapacidades(request.POST)
       # MiFormulario.fields['totalEmpresa']='0'
       # MiFormulario.fields['totalArl']='0'
       # MiFormulario.fields['totalAFP']='0'
       # MiFormulario.fields['totalEPS']='0'
       # MiFormulario.fields['totalIncapacidad']='0'
        
        if MiFormulario.is_valid():
             Objincapacidad = MiFormulario.save(commit=False)
             datosForm = MiFormulario.cleaned_data
             tipoIncapaci = datosForm.get('tipoIncapacidad')
             totalDias    = datosForm.get('totalDias')
             salarioDia   = float(datosForm.get('salarioDia'))
             if tipoIncapaci=='Enfermedad Comun':
                 if totalDias<3:
                   Objincapacidad.totalEmpresa= str(totalDias*salarioDia)
                   Objincapacidad.totalArl='0'
                   Objincapacidad.totalEPS='0'
                   Objincapacidad.totalAFP='0'
                   Objincapacidad.totalIncapacidad=str(totalDias*salarioDia)
                 elif totalDias < 181:
                   Objincapacidad.totalEmpresa= str(2*salarioDia)
                   Objincapacidad.totalArl='0'
                   Objincapacidad.totalEPS= str((totalDias-2)*salarioDia*0.6667)
                   Objincapacidad.totalAFP='0'
                   Objincapacidad.totalIncapacidad=str(float(Objincapacidad.totalEmpresa)+float(Objincapacidad.totalEPS))
                 elif totalDias < 541:
                   Objincapacidad.totalEmpresa= str(2*salarioDia)
                   Objincapacidad.totalArl='0'
                   Objincapacidad.totalEPS= str((178)*salarioDia*0.6667)
                   Objincapacidad.totalAFP= str((totalDias-180)*salarioDia*0.5)
                   Objincapacidad.totalIncapacidad=str(float(Objincapacidad.totalEmpresa)+float(Objincapacidad.totalEPS)+float(Objincapacidad.totalAFP))
                 else:
                   # temporalmente se implementa igual al intervalo anterior  
                   Objincapacidad.totalEmpresa= str(2*salarioDia)
                   Objincapacidad.totalArl='0'
                   Objincapacidad.totalEPS= str((178)*salarioDia*0.6667)
                   Objincapacidad.totalAFP= str((totalDias-180)*salarioDia*0.5)
                   Objincapacidad.totalIncapacidad=str(float(Objincapacidad.totalEmpresa)+float(Objincapacidad.totalEPS)+float(Objincapacidad.totalAFP))
                         
             elif tipoIncapaci == 'Licencia Mat-Pat': 
                   Objincapacidad.totalEmpresa= '0'
                   Objincapacidad.totalArl='0'
                   Objincapacidad.totalEPS= str((120)*salarioDia)
                   Objincapacidad.totalAFP= '0'
                   Objincapacidad.totalIncapacidad=str(float(Objincapacidad.totalEPS))
             elif (tipoIncapaci == 'Accidente Laboral'): 
                   Objincapacidad.totalEmpresa= '0'
                   Objincapacidad.totalArl= str((totalDias)*salarioDia)
                   Objincapacidad.totalEPS= '0'
                   Objincapacidad.totalAFP= '0'
                   Objincapacidad.totalIncapacidad=str(float(Objincapacidad.totalArl))
             elif ( tipoIncapaci == 'Enfermedad Laboral'):  
                   Objincapacidad.totalEmpresa= '0'
                   Objincapacidad.totalArl= str((totalDias)*salarioDia)
                   Objincapacidad.totalEPS= '0'
                   Objincapacidad.totalAFP= '0'
                   Objincapacidad.totalIncapacidad=str(float(Objincapacidad.totalArl))
             elif tipoIncapaci == 'Accidente de Transito': 
                   Objincapacidad.totalEmpresa= str(2*salarioDia)
                   Objincapacidad.totalArl= str((totalDias-2)*salarioDia*0.67)
                   Objincapacidad.totalEPS= '0'
                   Objincapacidad.totalAFP= '0'
                   Objincapacidad.totalIncapacidad=str(float(Objincapacidad.totalArl)+float(Objincapacidad.totalEmpresa))          
                       
          
             Objincapacidad.save()
             return redirect("listarInca")
        else:
             return render(request,"Ausentismos/formularios.html",{"tituloFormulario":"Registrar Incapacidad","actionFormulario":"/ausentismos/crear/","contenidoFormulario":MiFormulario})
    else:
        MiFormulario=FormularioIncapacidades()
        return render(request,"Ausentismos/formularios.html",{"tituloFormulario":"Registrar Incapacidad","actionFormulario":"/ausentismos/crear/","contenidoFormulario":MiFormulario})


def listarAusentismo(request):
    return render(request,"Ausentismos/listaE.html",{"tituloListado":"Lista de Incapacidades","lista":ausentismo.objects.filter()})

def editarAusentismo(request):
    if (request.method=='POST'):
        id_=request.POST['id']
        objIncapacidad=ausentismo.objects.get(id=id_)
        miFormulario=FormularioIncapacidades(request.POST,instance=objIncapacidad)
        if miFormulario.is_valid():
            miFormulario.save()
            return redirect("listarInca")
        else:
            return render(request,"Ausentismos/editar.html",{"tituloFormulario":"Editar Incapacidades","actionFormulario":"/ausentismos/editar/","contenidoFormulario":miFormulario,"id":id_})
        
    else:
        id_=request.GET['id']
        objIncapacidad=ausentismo.objects.get(id=id_)
        miFormulario=FormularioIncapacidades(instance=objIncapacidad)
        return render(request,"Ausentismos/editar.html",{"tituloFormulario":"Editar Incapacidades","actionFormulario":"/ausentismos/editar/","contenidoFormulario":miFormulario,"id":id_})
    

def eliminarAusentismo(request):
    id_=request.GET['id']
    objIncapacidad=ausentismo.objects.get(id=id_)
    objIncapacidad.delete()
    return redirect("listarInca")    