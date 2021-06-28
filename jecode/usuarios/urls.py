from django.urls import path

from . import views

urlpatterns = [
    path('cadastro/', views.Cadastro.as_view(), name='cadastro'),
]
