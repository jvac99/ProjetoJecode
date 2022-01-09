from django.urls import path

from . import views

app_name = 'quadros'

urlpatterns = [
    path('', views.index, name='index'),
    path('quadros/', views.quadros,
         name='quadros'),
    path('novo_quadro/',
         views.novo_quadro, name='novo_quadro'),
    path('editar_quadro/<int:id>',
         views.editar_quadro, name='editar_quadro'),
    path('deletar_quadro/<int:id>',
         views.deletar_quadro, name='deletar_quadro'),
    path('quadro/<int:id_quadro>/',
         views.quadro,
         name='quadro'),
]
