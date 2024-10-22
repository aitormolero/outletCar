from django.http import HttpResponse
from django.shortcuts import render
from .models import Coche, Marca, Categoria


# por cada marca obtener el coche con el precio mas alto y mostrarlo
def index(request):
    marcas = Marca.objects.all()
    coches = []

    for marca in marcas:
        coche = Coche.objects.filter(marca__id=marca.id).order_by('-precio').first()
        coches.append(coche)

    return HttpResponse(coches)

