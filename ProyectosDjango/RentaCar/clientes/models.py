from django.db import models

# Create your models here.
class Clientes(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.IntegerField()
    email=models.EmailField()
    fechaNacimi=models.DateField()
    

class Tipos(models.Model):
    nombre=models.CharField(max_length=20)
    descripcion=models.CharField(max_length=100)
    
    
 ## C R U D   

