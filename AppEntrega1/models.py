from django.db import models

# Create your models here.

class Peliculas(models.Model):
    nombre = models.CharField (max_length=30)
    genero = models.CharField (max_length=30)
    estreno = models.CharField (max_length=30)
    

class Series_Accion (models.Model):
   nombre = models.CharField (max_length=30)
   genero = models.CharField (max_length=30)
   temporadas = models.CharField (max_length=30)
   capitulos = models.CharField (max_length=30)
    
class Generos (models.Model):
    pass


class Comentarios (models.Model):
    pass