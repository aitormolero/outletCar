from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, View, DetailView
from .models import Coche, Marca, Categoria, COMBUSTIBLE_OPCIONES, TRANSMISION_OPCIONES, TRACCION_OPCIONES, NUMERO_PUERTAS_OPCIONES
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CocheForm
from django.utils.translation import gettext_lazy as _, activate
from django.shortcuts import redirect


def set_language(request):
    lang_code = request.GET.get('language')
    if lang_code:
        activate(lang_code)
        request.session['django_language'] = lang_code

        referer = request.META.get('HTTP_REFERER', '/')
        
        if '/es/' in referer:
            redirect_url = referer.replace('/es/', f'/{lang_code}/')
        elif '/en/' in referer:
            redirect_url = referer.replace('/en/', f'/{lang_code}/')
        else:
            redirect_url = f'/{lang_code}/'

        return redirect(redirect_url)

    return redirect('/')


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
            categoria_nombre = _("Híbrido / Eléctrico")

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

        # Aquí buscamos por el msgid original en lugar del traducido.
        if marca and marca != "Marca" and marca != "Brand":
            queryset = queryset.filter(marca__id=marca)
        if transmision and transmision != _("Transmisión"):
            # Buscar el msgid traducido
            opciones_transmision = {
                _("Manual"): "Manual",
                _("Automática"): "Automática"
            }
            transmision_original = opciones_transmision.get(transmision)
            if transmision_original:
                queryset = queryset.filter(transmision=transmision_original)
        if combustible and combustible != _("Combustible"):
            opciones_combustible = {
                _("Gasolina"): "Gasolina",
                _("Diésel"): "Diésel",
                _("Eléctrico"): "Eléctrico",
                _("Híbrido"): "Híbrido"
            }
            combustible_original = opciones_combustible.get(combustible)
            if combustible_original:
                queryset = queryset.filter(combustible=combustible_original)
        if traccion and traccion != _("Tracción"):
            opciones_traccion = {
                _("Delantera"): "Delantera",
                _("Trasera"): "Trasera",
                _("Total"): "Total"
            }
            traccion_original = opciones_traccion.get(traccion)
            if traccion_original:
                queryset = queryset.filter(traccion=traccion_original)
        if puertas and puertas != _("Puertas"):
            try:
                puertas = int(puertas)
                queryset = queryset.filter(numero_puertas=puertas)
            except ValueError:
                pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['marcas'] = Marca.objects.order_by('nombre').all()
        context['transmisiones'] = [ _("Manual"), _("Automática") ]
        context['combustibles'] = [ _("Gasolina"), _("Diésel"), _("Eléctrico"), _("Híbrido") ]
        context['tracciones'] = [ _("Delantera"), _("Trasera"), _("Total") ]
        context['num_puertas'] = [2, 4, 5]
        return context



class AgregarCocheView(TemplateView):
    template_name = 'agregar_coche_formulario.html'

    def get(self, request, *args, **kwargs):
        marcas = Marca.objects.all()
        categorias = Categoria.objects.all()
        form = CocheForm()
        return render(request, self.template_name, {
            "form": form,
            "marcas": marcas,
            "categorias": categorias,
            'combustibles': COMBUSTIBLE_OPCIONES,
            'tracciones': TRACCION_OPCIONES,
            'transmisiones': TRANSMISION_OPCIONES, 
            'numero_puertas': NUMERO_PUERTAS_OPCIONES
        })

    def post(self, request, *args, **kwargs):
        marcas = Marca.objects.all()
        categorias = Categoria.objects.all()
        form = CocheForm(request.POST, request.FILES)

        if form.is_valid():
            print("\n\nFormulario válido, ¡Coche agregado con éxito!\n\n")
            form.save()

            return redirect('index_coches')
        else:
            print("\n\nFormulario no válido")
            print(form.errors)

            return render(request, self.template_name, {
                "form": form,
                "marcas": marcas,
                "categorias": categorias,
                'combustibles': COMBUSTIBLE_OPCIONES,
                'tracciones': TRACCION_OPCIONES,
                'transmisiones': TRANSMISION_OPCIONES,
                'numero_puertas': NUMERO_PUERTAS_OPCIONES
            })


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
        print(_("¡Nueva Reseña de Coche!"))
        print("-" * 50)
        print(f"{_('Correo Electrónico')}: {email}")
        print(f"{_('DNI')}: {dni}")
        print(f"{_('Marca')}: {marca_id}")
        print(f"{_('Modelo')}: {modelo}")
        print(f"{_('Categoría')}: {categoria_id}")
        print(f"{_('Transmisión')}: {transmision}")
        print(f"{_('¿Es Descapotable?')} {'Sí' if descapotable == 'True' else 'No'}")
        print(f"{_('Recomendaciones')}: {recomendaciones}")
        print("-" * 50 + "\n\n")

        return HttpResponse(_("Formulario enviado con éxito."))

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
            categoria_nombre = _("Híbrido / Eléctrico")
        categoria = get_object_or_404(Categoria, nombre=categoria_nombre)
        context['categoria'] = categoria
        context['coches'] = Coche.objects.filter(categoria=categoria)
        return context