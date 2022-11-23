from django.db import models
from django.utils import timezone

class ausentismo(models.Model):
    nombres=models.CharField(max_length=80)
    apellidos=models.CharField(max_length=80)
    tipoId=models.CharField(max_length=10)
    identificacion=models.CharField(max_length=20)
    cargo=models.CharField(max_length=20)
    tipoIncapacidad=models.CharField(max_length=100)
    salario=models.CharField(max_length=80)
    eps=models.CharField(max_length=100,default="")
    afp=models.CharField(max_length=100,default="")
    arl=models.CharField(max_length=100,default="")
    salarioDia=models.CharField(max_length=10)
    fechaInicial=models.DateField(auto_now_add=True)
    fechaFinal=models.DateField(default=timezone.now())
    totalDias=models.IntegerField()
    clasificacion=models.CharField(max_length=10,default="")
    totalEmpresa=models.CharField(max_length=20,default="")
    totalArl=models.CharField(max_length=30,default="")
    totalAFP=models.CharField(max_length=30,default="")
    totalEPS=models.CharField(max_length=30,default="")
    totalIncapacidad=models.CharField(max_length=30,default="")
