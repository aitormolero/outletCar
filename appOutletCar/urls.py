from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('marca/<str:marca>/', views.index_marca, name='index_marca'),
    path('categoria/<str:categoria>/', views.index_categoria, name='index_categoria'),
]