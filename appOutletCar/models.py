from django.db import models

MANUAL = 'Manual'
AUTOMATICA = 'Automática'

TRANSMISION_OPCIONES = [
    (MANUAL, 'Manual'),
    (AUTOMATICA, 'Automática')
]


GASOLINA = 'Gasolina'
DIESEL = 'Diésel'
ELECTRICO = 'Eléctrico'
HIBRIDO = 'Híbrido'

COMBUSTIBLE_OPCIONES = [
    (GASOLINA, 'Gasolina'),
    (DIESEL, 'Diésel'),
    (ELECTRICO, 'Eléctrico'),
    (HIBRIDO, 'Híbrido')
]


DELANTERA = 'Delantera'
TRASERA = 'Trasera'
TOTAL = 'Total'

TRACCION_OPCIONES = [
    (DELANTERA, 'Delantera'),
    (TRASERA, 'Trasera'),
    (TOTAL, 'Total')
]


DOS = 2
CUATRO = 4
CINCO = 5

NUMERO_PUERTAS_OPCIONES = [
    (DOS, 2),
    (CUATRO, 4),
    (CINCO, 5)
]


class Marca (models.Model):
    nombre = models.CharField(max_length = 50)
    pais_origen = models.CharField(max_length = 50, blank = True, null = True)
    fecha_fundacion = models.DateField(blank = True, null = True)
    descripcion = models.TextField(blank = True, null = True)

    imagen = models.ImageField(upload_to = 'static/img/marcas', blank = True, null = True, verbose_name = 'Image')

    def __str__(self):
        return self.nombre


class Categoria (models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.nombre


class Coche (models.Model):
    anio = models.PositiveIntegerField(default = 2000)
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    color = models.CharField(max_length = 50, default = 'Blanco')
    kilometraje = models.PositiveIntegerField(default=0)
    transmision = models.CharField(max_length = 50, choices = TRANSMISION_OPCIONES)
    combustible = models.CharField(max_length = 50, choices = COMBUSTIBLE_OPCIONES)
    traccion = models.CharField(max_length = 50, choices = TRACCION_OPCIONES)
    numero_puertas = models.PositiveIntegerField(default = 4, choices = NUMERO_PUERTAS_OPCIONES)
    descapotable = models.BooleanField(default = False)
    descripcion = models.TextField(blank = True, null = True)

    marca = models.ForeignKey('Marca', on_delete = models.CASCADE)
    modelo = models.CharField(max_length = 100)
    categoria = models.ManyToManyField('Categoria')

    imagen = models.ImageField(upload_to = 'static/img/coches', blank = True, null = True, verbose_name = 'Image')

    def __str__(self):
        return str(self.marca) + ' ' + str(self.modelo) + " (" + str(self.anio) + ")"