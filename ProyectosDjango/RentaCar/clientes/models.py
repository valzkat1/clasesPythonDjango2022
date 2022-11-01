from tabnanny import verbose
from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField(blank=True,null=True)
    fechaNacimi=models.DateField(verbose_name="Fecha Nacimiento")
    def __str__(self):
        return 'Nombre: %s, Edad: %s, Email: %s, FechaN: %s'%(self.nombre,self.edad,self.email,self.fechaNacimi)
    
    

class Tipos(models.Model):
    nombre=models.CharField(max_length=20,verbose_name="Tipo Cliente")
    descripcion=models.CharField(max_length=100)
    def __str__(self):
        return 'Tipo: %s, Descripcion: %s '%(self.nombre,self.descripcion)
   
class Venta(models.Model):
    fecha=models.DateField()
    total=models.IntegerField()
    cliente=models.CharField(max_length=100)
    def __str__(self):
        return 'Fecha: %s, Total: %s, Cliente: %s '%(self.fecha,self.total,self.cliente)
        
 ## C R U D   

