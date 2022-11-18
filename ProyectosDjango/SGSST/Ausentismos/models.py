from django.db import models

class ausentismo(models.Model):
    nombres=models.CharField(max_length=80)
    apellidos=models.CharField(max_length=80)
    tipoId=models.CharField(max_length=10)
    identificacion=models.CharField(max_length=20)
    cargo=models.CharField(max_length=20)
    tipoIncapacidad=models.CharField(max_length=100)
    salario=models.CharField(max_length=80)
    eps=models.CharField(max_length=100)
    salarioDia=models.CharField(max_length=10)
    fechaInicial=models.DateField()
    fechaFinal=models.DateField()
    totalDias=models.IntegerField()
    clasificacion=models.CharField(max_length=10)
