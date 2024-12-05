from django import forms
from .models import Coche

class CocheForm(forms.ModelForm):
    class Meta:
        model = Coche
        fields = '__all__'
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'anio': 'Año',
            'precio': 'Precio',
            'color': 'Color',
            'kilometraje': 'Kilometraje',
            'transmision': 'Transmisión',
            'combustible': 'Combustible',
            'traccion': 'Tracción',
            'numero_puertas': 'Número de Puertas',
            'descapotable': '¿Es descapotable?',
            'descripcion': 'Descripción',
            'categoria': 'Categorías',
            'imagen': 'Imagen del coche',
        }
