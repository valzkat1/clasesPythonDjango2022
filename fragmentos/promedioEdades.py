# Realizar un programa que solicite al usuario las edades de 10 amigos y muestre su promedio
sumatoria=0
listaEdades=[]
cantidad=10
promedio=0.0

for i in range(10):
    print('Por favor ingrese la edad ',i)
    listaEdades.append(int(input()))
    sumatoria=sumatoria+listaEdades[i]

promedio=sumatoria/10
print('El promedio de edad es: ',promedio)    




