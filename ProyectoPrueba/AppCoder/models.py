from dataclasses import Field

from django.db import models

# Create your models here.
class Curso(models.Model):
   nombre=models.CharField("nombre", max_length=50)
   camada = models.IntegerField("camada")

class Estudiantes(models.Model):
   nombre=models.CharField("nombre", max_length=50)
   apellido = models.CharField("apellido", max_length=50)
   email = models.EmailField()

class Profesor(models.Model):
   nombre=models.CharField("nombre", max_length=50)
   apellido = models.CharField("apellido", max_length=50)
   email = models.EmailField()
   profesion= models.CharField("profesion", max_length=50)

class Entregable(models.Model):
   nombre=models.CharField("nombre", max_length=50)
   fecha = models.DateField("fecha", max_length=50)
   entregado = models.BooleanField()
 
class Familia(models.Model):
   nombre=models.CharField("nombre", max_length=50)
   apellido=models.CharField("apellido", max_length=50)
   dni = models.IntegerField("dni")
   fecha_nacimiento=models.CharField("fecha_nacimiento", max_length=50)