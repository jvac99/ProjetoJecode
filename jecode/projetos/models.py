from django.db import models
from django.contrib.auth import get_user_model

# Projeto: Projeto


class Projeto(models.Model):
    nome = models.CharField(max_length=255, null=False, blank=False)
    descricao = models.TextField(blank=True)
    usuario = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Lista: lista de atividades

class Lista(models.Model):
    nome = models.CharField(max_length=255)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Atividade

class Atividade(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField(blank=True)
    membros = models.ManyToManyField(get_user_model())
    #etiqueta = models.CharField(max_length=255)
    # = models.DateTimeField()
    opc = (
        ('pendente', 'Pendente'),
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    )
    status = models.CharField(max_length=10, choices=opc)
    requisitos = models.ManyToManyField('Atividade', blank=True)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
