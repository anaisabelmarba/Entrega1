from django.db import models

# Create your models here.

class Añadir(models.Model):
    nombre = models.CharField (max_length=30)
    genero = models.CharField (max_length=30)
    estreno = models.DateField()

    def __str__ (self):
        return self.nombre


class Peliculas(models.Model):
    nombre = models.CharField(max_length=20)
    genero = models.CharField(max_length=20)