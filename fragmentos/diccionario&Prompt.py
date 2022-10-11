
# Solicitar una fecha al usuario separando sus componentes en un diccionario por mes,año,dia
# Imprimir en consola el siguiente mensaje:  <dia> de <mes> del <año> 

# formato de fecha 2022/10/05

meses={1:'Enero',2:'Ferbrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}


print('Por favor ingrese la fecha (yyyy/mm/dd)')
fecha=input()

fechaArreglo=fecha.split('/')

diccionarioFecha={}
diccionarioFecha['dia']=fechaArreglo[2]
diccionarioFecha['mes']=meses[int(fechaArreglo[1])]
diccionarioFecha['ano']=fechaArreglo[0]

print('La fecha ingresada es: '+diccionarioFecha.get('dia')+' de '+diccionarioFecha.get('mes')+' del '+diccionarioFecha.get('ano'))




