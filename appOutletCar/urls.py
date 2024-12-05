from django.urls import path
from . import views
from .views import IndexView, AboutView, MarcaDetailView, CategoriaDetailView, CocheListView, ReseñaCocheView, GetCategoriesByBrandView, GetCarsByBrandAndCategoryView, ShowCocheView, ShowMarcaView, ShowCategoriaView, AgregarCocheView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='index_about'),
    path('coches/', CocheListView.as_view(), name='index_coches'),
    path('coches/<int:coche_id>/', ShowCocheView.as_view(), name='show_coche'),
    path('marcas/<str:marca>/', MarcaDetailView.as_view(), name='index_marca'),
    path('marcas/<str:marca>/detail/', ShowMarcaView.as_view(), name='show_marca'),
    path('categorias/<str:categoria>/', CategoriaDetailView.as_view(), name='index_categoria'),
    path('categorias/<str:categoria>/detail/', ShowCategoriaView.as_view(), name='show_categoria'),
    path('reseña/', ReseñaCocheView.as_view(), name='index_formulario'),
    path('añadir/', AgregarCocheView.as_view(), name='añadir_coche'),
    path('api/categorias/<int:marca_id>/', GetCategoriesByBrandView.as_view(), name='get_categories_by_brand'),
    path('api/coches/<int:marca_id>/<int:categoria_id>/', GetCarsByBrandAndCategoryView.as_view(), name='get_cars_by_brand_and_category'),
]