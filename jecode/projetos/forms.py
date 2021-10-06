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
        if Lista.objects.filter(nome=nome).exists():
            raise forms.ValidationError('Já existe uma lista com este nome.')

    class Meta:
        model = Lista
        fields = ['nome']
        nome = forms.CharField()


class AtividadeForm(forms.ModelForm):
    def clean(self):
        cleaned_data = super(AtividadeForm, self).clean()
        titulo = cleaned_data.get('titulo')
        if Atividade.objects.filter(titulo=titulo).exists():
            raise forms.ValidationError(
                'Já existe uma atividade com este titulo.')

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
        fields = ['titulo', 'descricao', 'lista']
        titulo = forms.CharField()
        descricao = forms.CharField()

