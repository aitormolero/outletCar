from django.urls import path
from .views import IndexView, AboutView, MarcaDetailView, CategoriaDetailView, CocheListView, ReseñaCocheView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='index_about'),
    path('marcas/<str:marca>/', MarcaDetailView.as_view(), name='index_marca'),
    path('categorias/<str:categoria>/', CategoriaDetailView.as_view(), name='index_categoria'),
    path('coches/', CocheListView.as_view(), name='index_coches'),
    path('reseña/', ReseñaCocheView.as_view(), name='index_formulario'),
]