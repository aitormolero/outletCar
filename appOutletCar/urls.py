from django.urls import path
from . import views
from .views import IndexView, AboutView, MarcaDetailView, CategoriaDetailView, CocheListView, ReseñaCocheView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view(), name='index_about'),
    path('coches/', CocheListView.as_view(), name='index_coches'),
    path('coches/<int:coche_id>/', views.show_coche, name='show_coche'),
    path('marcas/<str:marca>/', MarcaDetailView.as_view(), name='index_marca'),
    path('marcas/<str:marca>/detail/', views.show_marca, name='show_marca'),
    path('categorias/<str:categoria>/', CategoriaDetailView.as_view(), name='index_categoria'),
    path('categorias/<str:categoria>/detail/', views.show_categoria, name='show_categoria'),
    path('reseña/', ReseñaCocheView.as_view(), name='index_formulario'),
]