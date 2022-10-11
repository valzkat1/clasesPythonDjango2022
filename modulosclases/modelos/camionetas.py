from modelos.Automovil import Automovil

# Crear clase persona con atributos generales. y dos clases hijas Empleado, Cliente con atributos y metodos propios.
#Desde el main llenar un objeto de cada clase


#Herencia entre clases. 
class camionetas(Automovil):
    """" Clase que hereda de automovil """
    __puertas=6
    
    def __init__(self,puertas):
        self.__puertas=puertas
        super().__init__('Plata')
        
    def getPuertas(self):
        return self.__puertas 
    
    def setPuertas(self,puertas):
        self.__puertas=puertas   
        
    def parametroReferencia(self,objet):
        objet=objet*2
        