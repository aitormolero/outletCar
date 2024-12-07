from django.contrib import admin
from .models import Coche, Marca, Categoria



class CocheAdmin(admin.ModelAdmin):

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