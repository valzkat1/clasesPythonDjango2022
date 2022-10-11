class Humanos:
    def formaComunicacion(self):
        return "Oral"
    
    def formaComunicacion(self,texto):
        return "Poli local"
    
    def formaComunicacion(self,texto,numero):
        return " "+texto
    
    

                
                
human1=Humanos()     
#print(human1.formaComunicacion("informacion"))

print(human1.formaComunicacion("Texto cualquiera",10))
           
           
