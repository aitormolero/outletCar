from django import forms
from django.utils.translation import gettext_lazy as _  
from .models import Coche

class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = '__all__'
        labels = {
            'marca': _('Marca'),
            'modelo': _('Modelo'),
            'anio': _('Año'),
            'precio': _('Precio'),
            'color': _('Color'),
            'kilometraje': _('Kilometraje'),
            'transmision': _('Transmisión'),
            'combustible': _('Combustible'),
            'traccion': _('Tracción'),
            'numero_puertas': _('Número de Puertas'),
            'descapotable': _('¿Es descapotable?'),
            'descripcion': _('Descripción'),
            'categoria': _('Categorías'),
            'imagen': _('Imagen del coche'),
        }
