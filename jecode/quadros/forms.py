from django import forms
from .models import *


class QuadroForm(forms.ModelForm):
    class Meta:
        model = Quadro
        fields = ['nome', 'descricao']
        nome = forms.CharField()
        descricao = forms.CharField()
