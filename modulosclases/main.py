#Patron de diseño MVC
# Html, css y javascript  (FrontEnd) Typescript  -- React, Angular


#Importar un modulo
from modelos import Usuario
#import modelos.Automovil
from modelos.Automovil import Automovil
from modelos.camionetas import camionetas

print(Usuario.funcionSumar2(10,23))

print(Usuario.getMinombre())

obj1=Automovil('azul')
obj1.setMarca('Audi')
(obj1.mostrarDatos())

obj2=camionetas(5)

obj2.setMarca('Mazda')

obj2.mostrarDatos()

varObjet=int(10)
print(varObjet)
obj2.parametroReferencia(varObjet)
print(varObjet)

def nombreFuncion():
    print('Funcion llamada')




def crearLista(maximo):
    inicial=1
    listaCreada=[]
    while inicial<maximo:
        listaCreada.append(inicial*3)
        inicial=inicial+1
    return listaCreada
print(crearLista(10))


def crearListaGen(maximo):
    inicial=1
    while inicial<maximo:
        yield inicial*3
        inicial=inicial+1
iteraciones=crearListaGen(4)       
print('Primer Elemento')
print(iteraciones.__next__()) 
print('Segunda Iteracion')
print(iteraciones.__next__())  
print('Tercera Iteracion')
print(iteraciones.__next__())
print('Cuarda Iteracion')



lista1=[1,2,3,4,5,6,7,8]  

listaIterable=iter(lista1)  
print('*************')

try:
    print(next(listaIterable))
    print(next(listaIterable))
    print(next(listaIterable))
    print(next(listaIterable))
    print(next(listaIterable))
    print(next(listaIterable))
    print(next(listaIterable))
    print(next(listaIterable))
    print(next(listaIterable))      
except StopIteration:
    print("Error capturado en cantidad de iteraciones")
except IOError:    
    print("Error de plataforma windows")
except: 
    print("Error no identificado")   
        
    


    
    






