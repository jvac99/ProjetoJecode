from django import forms
from .models import *


class ProjetoForm(forms.ModelForm):
    class Meta:
        model = Projeto
        fields = ['nome', 'descricao']
        nome = forms.CharField()
        descricao = forms.CharField()


class ListaForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(ListaForm, self).clean()
        nome = cleaned_data.get('nome')

    class Meta:
        model = Lista
        fields = ['nome']
        nome = forms.CharField()


class AtividadeForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(AtividadeForm, self).clean()
        titulo = cleaned_data.get('titulo')

    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao']
        titulo = forms.CharField()
        descricao = forms.CharField()


class AtividadeFormEditar(forms.ModelForm):
    def clean(self):
        cleaned_data = super(AtividadeFormEditar, self).clean()

    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao', 'lista', 'requisitos']
        titulo = forms.CharField()
        descricao = forms.CharField()


class SubatividadeForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(SubatividadeForm, self).clean()
        titulo = cleaned_data.get('titulo')

    class Meta:
        model = Subatividade
        fields = ['titulo', 'descricao']
        titulo = forms.CharField()
        descricao = forms.CharField()


class SubatividadeFormEditar(forms.ModelForm):
    def clean(self):
        cleaned_data = super(SubatividadeFormEditar, self).clean()

    class Meta:
        model = Atividade
        fields = ['titulo', 'descricao']
        titulo = forms.CharField()
        descricao = forms.CharField()
