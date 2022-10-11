# Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
# arañara

print('Por favor ingrese la palabra a evaluar')
palabra=input()

listaDerecho=list(palabra)
listaReves=list(palabra)
listaReves.reverse()

if listaDerecho==listaReves:
    print('Es un palindromo')
else:
    print('No es palindromo')    
    
    
   



