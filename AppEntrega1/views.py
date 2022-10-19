
from http.client import HTTPResponse
from django.shortcuts import render
from AppEntrega1.models import Peliculas
# Create your views here.
def Inicio(request):
    return render(request, "EntregaCoder/Inicio.html")
def Añadir (request):
    return render(request, "EntregaCoder/Añadir.html")
def Peliculas(request):
    return render(request, "EntregaCoder/Peliculas.html")
def busqueda_peliculas(request):
    return render(request, "EntregaCoder/Busqueda_Pelis.html")
def Pelicula_Buscada(request):
    if request.method == "POST":
        pel = request.post["pelis"]
        peliculas = Peliculas.objects.filter(nombre__icontains=pel)
        return render(request, "EntregaCoder/Peliculas.html", {"peliculas": peliculas, "query":pel })


    else:
        mensaje = "No has escrito nada"

    return HTTPResponse(mensaje)
