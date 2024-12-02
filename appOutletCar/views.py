from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView, ListView, DetailView
from .models import Coche, Marca, Categoria


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
