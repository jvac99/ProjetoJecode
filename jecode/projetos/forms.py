from django import forms
from .models import *


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ('nome', 'descricao')


class ListaForm(forms.ModelForm):
    class Meta:
        model = Lista
        fields = ('nome',)


class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividade
        fields = ('titulo', 'descricao')
