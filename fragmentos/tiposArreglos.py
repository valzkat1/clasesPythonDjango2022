
#Listas normales
listaUno=[1,7,3,4,1,6,7,8,9]
print(listaUno[-2])
#Adicionar elementos a la lista
listaUno.append(10)
print(listaUno)
#Ordenar lista 
listaUno.sort()
print('******** lista Sort *')
print(listaUno)




#Listas tipo dict
listaDos={'uno':1,'dos':2,'tres':3}
listaTres= dict(uno=1,dos=2,tres=3)

print(listaDos['dos'])
print(listaTres['uno'])

#Recorrido de diccionarios normal impresin de 'Key'
for elementoDict in listaDos.keys():
    print(elementoDict)


for elementoDicta in listaTres.values():
    print(elementoDicta)
    
    
for elmenetoDicciona in listaDos.items():
    print(elmenetoDicciona)    










