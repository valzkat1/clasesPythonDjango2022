
# Patron de Diseño de software  (Modelo, Vista, Controlador) MVC
# Escribir un programa que pregunte al usuario los números ganadores de la lotería de Bogota, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
print('Por favor ingrese la cantidad de resultados')
cantidadNumeros=int(input())
indice=0
listaGanadores=[]
# Ambito o Scope de las variables

while indice<cantidadNumeros:
    indice=indice+1
    print('Por favor ingrese el resultado ',indice)
    listaGanadores.append(int(input()))
listaGanadores.sort()
print(listaGanadores)        
    
    
    
    
    










