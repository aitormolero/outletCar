from django.http import HttpResponse
from django.shortcuts import render
from .models import Coche, Marca, Categoria


# Función para obtener por cada marca obtener el coche con el precio mas alto y mostrarlo
def index(request):
    marcas = Marca.objects.all()
    coches = []

    for marca in marcas:
        coche = Coche.objects.filter(marca__id=marca.id).order_by('-precio').first()
        coches.append(coche)

    context = {
        'coches': coches,
    }

    return render(request, 'index.html', context)

# Función para obtener todos los coches de una marca
def index_marca(request, marca):

    coches_all = Coche.objects.all()
    coches_marca = []
    for coche in coches_all:
        if(coche.marca.id == int(marca)):
            coches_marca.append(coche)

    context = {
        'coches': coches_marca,
    }

    return render(request, 'index.html', context)

# Función para obtener todos los coches de una categoría    
def index_categoria(request, categoria):

    coches_all = Coche.objects.all()
    coches_categoría = []
    
    for coche in coches_all:
        if(coche.categoria == categoria):
            coches_categoría.append(coche)

    context = {
        'coches': coches_categoría,
    }

    return render(request, 'index.html', context)
       

