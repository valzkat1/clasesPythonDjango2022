
import tkinter as tk
from tkinter import simpledialog

meses={1:'Enero',2:'Ferbrero',3:'Marzo',4:'Abril',5:'Mayo',6:'Junio',7:'Julio',8:'Agosto',9:'Septiembre',10:'Octubre',11:'Noviembre',12:'Diciembre'}

ROOT=tk.Tk()

ROOT.withdraw()

fecha=simpledialog.askstring(title='Formato de fechas',prompt='Por favor ingrese una fecha (yyyy/mm/dd)')

fechaArreglo=fecha.split('/')

diccionarioFecha={}
diccionarioFecha['dia']=fechaArreglo[2]
diccionarioFecha['mes']=meses[int(fechaArreglo[1])]
diccionarioFecha['ano']=fechaArreglo[0]

simpledialog.askstring(title='Resultado',prompt='La fecha ingresada es: '+diccionarioFecha.get('dia')+' de '+diccionarioFecha.get('mes')+' del '+diccionarioFecha.get('ano'))

# POO Python, Herencia, Polimirfismo, encapsulamiento etc.





