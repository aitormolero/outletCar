from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Coche, Marca, Categoria
from django.shortcuts import render, get_object_or_404

class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        marcas = Marca.objects.all()
        coches = [Coche.objects.filter(marca__id=marca.id).order_by('-precio').first() for marca in marcas]
        context['coches'] = coches
        return context


class AboutView(TemplateView):
    template_name = 'about.html'


class MarcaDetailView(TemplateView):
    template_name = 'marcas.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        marca_nombre = self.kwargs['marca'].lower()
        coches_all = Coche.objects.all()
        coches_marca = [coche for coche in coches_all if coche.marca.nombre.lower() == marca_nombre]

        context['coches'] = coches_marca
        context['marcas'] = Marca.objects.all()
        context['marca_seleccionada'] = Marca.objects.get(nombre__iexact=self.kwargs['marca'])
        return context


class CategoriaDetailView(TemplateView):
    template_name = 'categorias.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_nombre = self.kwargs['categoria']
        if categoria_nombre == "HibridoElectrico":
            categoria_nombre = "Híbrido / Eléctrico"

        coches_all = Coche.objects.all()
        coches_categoria = [
            coche for coche in coches_all for cat in coche.categoria.all() if cat.nombre == categoria_nombre
        ]

        context['coches'] = coches_categoria
        context['categorias'] = Categoria.objects.all()
        context['categoria_activa'] = Categoria.objects.get(nombre=categoria_nombre)
        return context


class CocheListView(ListView):
    model = Coche
    template_name = 'car.html'
    context_object_name = 'coches'

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-precio')
        marca = self.request.GET.get('marca')
        transmision = self.request.GET.get('transmision')
        combustible = self.request.GET.get('combustible')
        traccion = self.request.GET.get('traccion')
        puertas = self.request.GET.get('puertas')

        if marca and marca != "Marca":
            queryset = queryset.filter(marca__id=marca)
        if transmision and transmision != "Transmisión":
            queryset = queryset.filter(transmision=transmision)
        if combustible and combustible != "Combustible":
            queryset = queryset.filter(combustible=combustible)
        if traccion and traccion != "Tracción":
            queryset = queryset.filter(traccion=traccion)
        if puertas and puertas != "Puertas":
            queryset = queryset.filter(numero_puertas=puertas)
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Marca.objects.order_by('nombre').all()
        context['transmisiones'] = ["Manual", "Automática"]
        context['combustibles'] = ["Gasolina", "Diésel", "Eléctrico", "Híbrido"]
        context['tracciones'] = ["Delantera", "Trasera", "Total"]
        context['num_puertas'] = [2, 4, 5]
        return context


class ReseñaCocheView(TemplateView):
    template_name = 'formulario.html'

    def get(self, request, *args, **kwargs):
        marcas = Marca.objects.all()
        categorias = Categoria.objects.all()
        coches = Coche.objects.all()
        
        return render(request, self.template_name, {
            "marcas": marcas,
            "categorias": categorias,
            "coches": coches
        })

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        dni = request.POST.get('dni')
        marca_id = request.POST.get('marca')
        modelo = request.POST.get('modelo')
        categoria_id = request.POST.get('categoria')
        transmision = request.POST.get('transmision')
        descapotable = request.POST.get('descapotable')
        recomendaciones = request.POST.get('recomendaciones')

        print("\n\n" + "-"*50)
        print("¡Nueva Reseña de Coche!")
        print("-" * 50)
        print(f"Correo Electrónico: {email}")
        print(f"DNI: {dni}")
        print(f"Marca: {marca_id}")
        print(f"Modelo: {modelo}")
        print(f"Categoría: {categoria_id}")
        print(f"Transmisión: {transmision}")
        print(f"¿Es Descapotable? {'Sí' if descapotable == 'True' else 'No'}")
        print(f"Recomendaciones: {recomendaciones}")
        print("-" * 50 + "\n\n")

        return HttpResponse("Formulario enviado con éxito.")


class GetCategoriesByBrandView(View):
    def get(self, request, marca_id):
        categorias = Categoria.objects.filter(coche__marca_id=marca_id).distinct()
        data = [{"id": categoria.id, "nombre": categoria.nombre} for categoria in categorias]
        return JsonResponse(data, safe=False)


class GetCarsByBrandAndCategoryView(View):
    def get(self, request, marca_id, categoria_id):
        coches = Coche.objects.filter(marca_id=marca_id, categoria__id=categoria_id).distinct()
        data = [{"id": coche.id, "modelo": coche.modelo} for coche in coches]
        return JsonResponse(data, safe=False)



class ShowCocheView(DetailView):
    model = Coche
    template_name = 'car_detail.html'
    context_object_name = 'coche'

    def get_object(self):
        return get_object_or_404(Coche, pk=self.kwargs['coche_id'])

class ShowMarcaView(TemplateView):
    template_name = 'marca_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        marca = get_object_or_404(Marca, nombre=self.kwargs['marca'])
        context['marca'] = marca
        context['coches'] = Coche.objects.filter(marca=marca)
        return context

class ShowCategoriaView(TemplateView):
    template_name = 'categoria_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        categoria_nombre = self.kwargs['categoria']
        if categoria_nombre == "HibridoElectrico":
            categoria_nombre = "Híbrido / Eléctrico"
        categoria = get_object_or_404(Categoria, nombre=categoria_nombre)
        context['categoria'] = categoria
        context['coches'] = Coche.objects.filter(categoria=categoria)
        return context
