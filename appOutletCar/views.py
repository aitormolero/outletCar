from django.http import HttpResponse
from django.shortcuts import redirect, render
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
        if((coche.marca.nombre).lower() == marca.lower()):
            
            coches_marca.append(coche)
    
    marcas = Marca.objects.all()

    context = {
        'coches': coches_marca,
        'marcas': marcas,
    }
	 
    return render(request, 'marcas.html', context)

# Función para obtener todos los coches de una categoría    
def index_categoria(request, categoria):

    if categoria == "HibridoElectrico":
        categoria = "Híbrido / Eléctrico"

    categorias = Categoria.objects.all()
    coches_all = Coche.objects.all()
    coches_categoría = []
    
    for coche in coches_all:
        for cat in coche.categoria.all():
            if(cat.nombre == categoria):
                coches_categoría.append(coche)

    context = {
        'coches': coches_categoría,
        'categorias': categorias,
        'categoria_activa': categoria,
    }

    return render(request, 'categorias.html', context)
       

def index_coches(request):
    coches = Coche.objects.order_by('-precio').all()

    marca = request.GET.get('marca')
    transmision = request.GET.get('transmision')
    combustible = request.GET.get('combustible')
    traccion = request.GET.get('traccion')
    puertas = request.GET.get('puertas')



    # Aplicar filtros solo si los valores no son los predeterminados
    if marca and marca != "Marca":
        coches = coches.filter(marca__id=marca)
    if transmision and transmision != "Transmisión":
        coches = coches.filter(transmision=transmision)
    if combustible and combustible != "Combustible":
        coches = coches.filter(combustible=combustible)
    if traccion and traccion != "Tracción":
        coches = coches.filter(traccion=traccion)
    if puertas and puertas != "Puertas":
        coches = coches.filter(numero_puertas=puertas)


    # Filtros
    marcas = Marca.objects.order_by('nombre').all()
    transmisiones = ["Manual", "Automática"]
    combustibles = ["Gasolina", "Diésel", "Eléctrico", "Híbrido"]
    tracciones = ["Delantera", "Trasera", "Total"]
    num_puertas = [2, 4, 5]


    context = {
        'coches': coches,
        'marcas': marcas,
        'transmisiones': transmisiones,
        'combustibles': combustibles,
        'tracciones': tracciones,
        'num_puertas': num_puertas,

    }

    return render(request, 'car.html', context)

