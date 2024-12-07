from django.contrib import admin
from .models import Coche, Marca, Categoria


admin.site.site_header = "Panel de Administración de Outlet Car"
admin.site.site_title = "Outlet Car Admin"
admin.site.index_title = "Gestión de Coches, Marcas y Categorías"

class CocheAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'anio', 'precio')
    list_filter = ('marca', 'categoria')
    search_fields = ('modelo', 'marca__nombre')
    ordering = ('marca', 'precio')

    fieldsets = (
        ('Datos Principales', {'fields': ('marca', 'modelo', 'anio', 'categoria')}),
        ('Especificaciones Técnicas', {
            'fields': ('kilometraje', 'color', 'transmision', 'combustible', 'traccion', 'numero_puertas', 'descapotable'),
            'description': 'Características técnicas del coche'
        }),
        ('Información Comercial', {'fields': ('precio', 'descripcion', 'imagen')}),
    )

    filter_horizontal = ('categoria',)  
    autocomplete_fields = ['marca']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name="Cliente").exists():
            return qs # Clientes pueden ver todos los coches
        return qs

    def has_add_permission(self, request):
        return not request.user.groups.filter(name="Cliente").exists()

    def has_change_permission(self, request, obj=None):
        return not request.user.groups.filter(name="Cliente").exists()

    def has_delete_permission(self, request, obj=None):
        return not request.user.groups.filter(name="Cliente").exists()
    

class MarcaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_fundacion', 'pais_origen')
    list_filter = ['pais_origen']
    search_fields = ('nombre', 'pais_origen')
    ordering = ['fecha_fundacion']

    fieldsets = (
        ('Datos Principales', {'fields': ('nombre', 'descripcion')}),
        ('Detalles Adicionales', {
            'fields': ('pais_origen', 'fecha_fundacion', 'imagen'),
            'description': 'Información opcional sobre la marca'
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name="Cliente").exists() or request.user.groups.filter(name="Vendedor").exists():
            return qs  # Clientes y vendedores pueden ver todas las marcas
        return qs

    def has_add_permission(self, request):
        return request.user.groups.filter(name="Administrador").exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name="Administrador").exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name="Administrador").exists()


class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre']
    list_filter = ['nombre']
    search_fields = ['nombre']
    ordering = ['nombre']
    
    fieldsets = (
        ('Datos Principales', {'fields': ('nombre',)}),
        ('Detalles Opcionales', {'fields': ('descripcion',)}),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.groups.filter(name="Cliente").exists() or request.user.groups.filter(name="Vendedor").exists():
            return qs  # Clientes y vendedores pueden ver todas las categorías
        return qs

    def has_add_permission(self, request):
        return request.user.groups.filter(name="Administrador").exists()

    def has_change_permission(self, request, obj=None):
        return request.user.groups.filter(name="Administrador").exists()

    def has_delete_permission(self, request, obj=None):
        return request.user.groups.filter(name="Administrador").exists()
    

# Registrar modelos personalizados
admin.site.register(Coche, CocheAdmin)
admin.site.register(Marca, MarcaAdmin)
admin.site.register(Categoria, CategoriaAdmin)