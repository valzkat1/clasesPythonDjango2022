#Calcular el promedio para una cantidad de estudiantes dada por el usuario con base a la cantidad
# de calificaciones que el usuario determine. (manejo de excepciones, generadores y ventana grafica.)
# Imprimir el nombre del estudiante y su respectivo promedio al frente.
import tkinter as tk
from tkinter import simpledialog

ROOT=tk.Tk()
ROOT.withdraw()


numEstu=0
numNota=0
isNumberEst=False
isNumberNot=False

listaEstudiantes=[]
listaPromedios=[]

def SolicitarInfo(mensaje):
    return simpledialog.askstring(title='Promedios',prompt=mensaje)




while isNumberEst==False:
    numEstu=SolicitarInfo("Por favor ingrese la cantidad de estudiantes")
    try:
      numEstu=int(numEstu)
      isNumberEst=True
    except ValueError as er:
        isNumberEst=False
        print(er)

while isNumberNot==False:
    numNota=SolicitarInfo("Por favor ingrese la cantidad de calificaciones a promediar.")
    try:
        numNota=int(numNota)
        isNumberNot=True
    except ValueError:
        print("Formato de numero incorrecto")
        isNumberNot=False 
        
        
for i in range(numEstu):
    sumatoria=0
    listaEstudiantes.append(SolicitarInfo("Nombre del estudiante "+str(i+1)))        
    for j in range(numNota):
        sumatoria=sumatoria+simpledialog.askfloat(title="Promedios",prompt="Por favor ingrese la nota "+str(j+1)+" de "+listaEstudiantes[i])
    listaPromedios.append(sumatoria/numNota)
    
iterableNotas=iter(listaPromedios)
iterableEstud=iter(listaEstudiantes)

for i in range(numEstu):
    #next(iterableEstud)
    print("El estudiante "+iterableEstud.__next__()+" tiene promedio: "+str(iterableNotas.__next__()))
    

