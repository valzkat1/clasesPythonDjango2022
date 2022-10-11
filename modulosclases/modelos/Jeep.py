from tkinter import Variable
from modelos.camionetas import camionetas


class Jeep(camionetas):
    vari=0
    
    def __init__(self, puertas):
        super().__init__(puertas)