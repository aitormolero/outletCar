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
INTEGRAL = 'Integral'
TRACCION_OPCIONES = [
    (DELANTERA, 'Delantera'),
    (TRASERA, 'Trasera'),
    (INTEGRAL, 'Integral')
]

DOS = 2
CUATRO = 4
CINCO = 5
NUMERO_PUERTAS_OPCIONES = [
    (DOS, 2),
    (CUATRO, 4),
    (CINCO, 5)
]


class Coche (models.Model):
    anio = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits = 10, decimal_places = 2)
    color = models.CharField(max_length = 50, blank = True, null = True)
    kilometraje = models.PositiveIntegerField(blank = True, null = True)
    transmision = models.CharField(max_length = 50, choices = TRANSMISION_OPCIONES)
    combustible = models.CharField(max_length = 50, choices = COMBUSTIBLE_OPCIONES)
    traccion = models.CharField(max_length = 50, choices = TRACCION_OPCIONES)
    numero_puertas = models.PositiveIntegerField(default = 4, choices = NUMERO_PUERTAS_OPCIONES)
    descripcion = models.TextField(blank = True, null = True)

    marca = models.ForeignKey('Marca', on_delete = models.CASCADE)
    modelo = models.CharField(max_length = 100)
    categoria = models.ManyToManyField('Categoria')

    def __str__(self):
        return self.marca + ' ' + self.modelo


class Marca (models.Model):
    nombre = models.CharField(max_length = 50)
    pais_origen = models.CharField(max_length = 50, blank = True, null = True)
    fecha_fundacion = models.DateField(blank = True, null = True)
    descripcion = models.TextField(blank = True, null = True)

    def __str__(self):
        return "(" + self.fecha_fundacion + ") " + self.nombre


class Categoria (models.Model):
    nombre = models.CharField(max_length = 50)
    descripcion = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.nombre