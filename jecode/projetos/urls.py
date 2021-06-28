from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inicio/', views.inicio, name='inicio'),
    path('listas_de_projetos/', views.listas_de_projetos, name='listas_de_projetos'),
    path('editar_projeto/<int:id>',
         views.editar_projeto, name='editar_projeto'),
    path('deletar_projeto/<int:id>',
         views.deletar_projeto, name='deletar_projeto'),
    path('detalhes_do_projeto/<int:id>',
         views.detalhes_do_projeto, name='detalhes_do_projeto'),
    path('lista_de_listas_do_projeto/<int:id>',
         views.lista_de_listas_do_projeto, name='lista_de_listas_do_projeto'),
    path('editar_lista_do_projeto/<int:id>',
         views.editar_lista_do_projeto, name='editar_lista_do_projeto'),
    path('deletar_lista_do_projeto/<int:id>',
         views.deletar_lista_do_projeto, name='deleta_lista_do_projeto'),
    path('detalhes_da_atividade_do_projeto/<int:id>',
         views.detalhes_da_atividade_do_projeto, name='detalhes_da_atividade_do_projeto'),
    path('lista_de_atividades_do_projeto/<int:id>',
         views.lista_de_atividades_do_projeto, name='lista_de_atividades_do_projeto'),
    path('editar_atividade_do_projeto/<int:id>',
         views.editar_atividade_do_projeto, name='editar_atividade_do_projeto'),
    path('deletar_atividade_do_projeto/<int:id>',
         views.deletar_atividade_do_projeto, name='deletar_atividade_do_projeto'),
]
