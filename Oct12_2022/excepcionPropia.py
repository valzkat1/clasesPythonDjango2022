class excepcionPropia(Exception):
    pass

    def __init__(self,mensaje):
        self.mensaje=mensaje
        super().__init__(mensaje)

    
    