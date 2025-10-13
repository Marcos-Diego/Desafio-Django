from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_de_receitas, name='lista_de_receitas'),
    path('<int:pk>/', views.detalhe_da_receita, name='detalhe_da_receita'),
    path('adicionar/', views.adicionar_receita, name='adicionar_receita'),
]
