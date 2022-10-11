# Tuplas 
tuplaUno=(1,2,3,4,5,6,7,8,9)
print(tuplaUno[5])

for elementoTupla in tuplaUno:
    print(elementoTupla)
    


# Clase set (Tipos set en python)  Representa conjuntos ordenados de elementos unicos
listaInicial=[1,1,3,4,7,4,7,9,8,2,1,9]

print('***********************')

listaSinRepetidos=set(listaInicial)
for datoLista in listaSinRepetidos:
    print(datoLista)

    
listaPalabra=set('Bienvenidos al curso de python con Django etc.') 
print(listaPalabra)

#listaPalabra.

print(listaPalabra)

print('***********************')


# Inmutabilidad 
listaPalabra2=frozenset('Bienvenidos al curso de python con Django etc.') 
print(listaPalabra2)
#listaPalabra2.

print('Rangos******************************')

# Clase range
print(list(range(10)))

for i in range(1,50):
    if i%2==0:
        print(i)
    else:
        continue    










  
    


