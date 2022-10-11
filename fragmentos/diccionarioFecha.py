# Solicitar una fecha al usuario separando sus componentes en un diccionario por mes,año,dia
# Imprimir en consola el siguiente mensaje:  <dia> de <mes> del <año> 


meses={1:'Enero',2:'Febrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}

fecha=[]

fechaText=input('fecha formato yy/mm/dd  ');
fechaListT=fechaText.split('/')

fecha.append({"dia":fechaListT[2]})
fecha.append({"mes":meses[int(fechaListT[1])]})
fecha.append({"ano":fechaListT[0]})

print(fecha)

