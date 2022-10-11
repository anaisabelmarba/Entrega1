
from django.shortcuts import render
# Create your views here.

def Inicio(request):
    return render(request, "EntregaCoder/Inicio.html")
def Generos (request):
    return render(request, "EntregaCoder/Generos.html")
def Peliculas(request):
    return render(request, "EntregaCoder/Peliculas.html")
def Series(request):
    return render(request, "EntregaCoder/Series.html")
def Comentarios(request):
    return render(request, "EntregaCoder/Comentarios.html")

