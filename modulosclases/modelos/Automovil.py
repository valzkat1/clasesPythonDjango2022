class Automovil:
    """" Clase de atributos genericos para los automoviles """
    
    #Encapsulamiento (Publico, Protegido y privado)
    #Scope o ambito de las variables

    color         =''
    _marca        =''
    __fabricacion =0
    
    
    def __init__(self,colo):
        self.color=colo
    
    
    def mostrarDatos(self):
        print(self.color+"  "+self._marca)
        return self.color
    
    def getMarca(self):
       return self._marca
        
    def setMarca(self,marca):
        self._marca=marca
    