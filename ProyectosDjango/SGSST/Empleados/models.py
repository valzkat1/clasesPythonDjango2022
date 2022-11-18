from django.db import models

class empleado(models.Model):
    nombres=models.CharField(max_length=80)
    apellidos=models.CharField(max_length=80)
    tipoId=models.CharField(max_length=10)
    identificacion=models.CharField(max_length=20)
    cargo=models.CharField(max_length=20)
    doc_arl=models.CharField(max_length=100)
    doc_afp=models.CharField(max_length=80)
    doc_eps=models.CharField(max_length=100)
