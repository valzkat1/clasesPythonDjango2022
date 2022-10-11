
condicion=True


# Condicional if.. else
if condicion:
    print('Condicion verdadera')
else:
    print('Condicion es falsa')   


contador=10
# Condicional if.. elif..  else..
if contador<0:
    print('Contador negativo')
elif contador<10:
    print('Contador menor a 10')
elif contador>10:
    print('Hay mas de 10 unidades')
else:
    print('Hay 10 unidades')            


 
x=0
# Condicional Anidado
if x<0:
    print('Negativo')
else:
    if x>0:
        print('Postivo')
    else:
        print('Cero')
print('Se ha cerrado el condicional')            
               
    
# While (Bucle)  
while condicion:
    print('La condicion debe ser falsa para salir')
    x=x+1
    if x>3:
        condicion=False
else:
    print('La condicion ya es falsa')    
 
 
 
condicion=True
x=0 
# While (Bucle)  con break
while condicion:
    x=x+1
    print('La condicion debe ser falsa para salir ',x)
    if x>3:
        break
else:
    print('La condicion ya es falsa') 
  
    
     
condicion=True
x=0
#Lista Numeros Naturales hasta el 16
numeros=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
#Lista con diferente tipado.
listaOtros=['uno','cinco',2,3,9,11,False]
print(listaOtros[0])
#print(listaOtros[-1])


# For con continue 
for numer in numeros:
    if numer%2==0:
        print(numer)
    else:
        continue  
    
        
# For con break
x=0
for numer in numeros:
    x=x+1
    if numer==8:
        print('Encontrado en la posicion ',x)        
        break
    else:
        print('Buscando Numero 8 ',x, ' veces')
 

