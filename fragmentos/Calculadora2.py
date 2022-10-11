
#print('')
print('Por favor seleccione la operacion a realizar: \n1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir')



opcion=(input())
resultado=0
print('Por favor ingrese el primer numero')
num1=int(input())

print('Por favor ingrese el segundo numero')
num2=int(input())

if opcion=='1':
    resultado=num1+num2
if opcion=='2':
    resultado=num1-num2
if opcion=='3':
    resultado=num1*num2
if opcion=='4':
    resultado=num1/num2

print('El resultado es ',resultado)                
