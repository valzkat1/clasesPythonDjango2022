from django.db import models

class usuario(models.Model):
    nombreusuario=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    rol=models.CharField(max_length=10)
    idEmpleado=models.IntegerField()

