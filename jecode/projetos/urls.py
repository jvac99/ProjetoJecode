from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('inicio/', views.inicio, name='inicio'),
    path('projetos_lista/', views.projetos_lista, name='projetos_lista'),
    path('projeto_detalhes/<int:id>',
         views.projeto_detalhes, name='projeto_detalhes'),
    path('delete/<int:id>',
         views.deleteProjeto, name='delete'),
]
