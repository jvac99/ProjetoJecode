from django.db import models
from django.contrib.auth.models import User

# Projeto: Projeto


class Projeto(models.Model):
    nome = models.CharField(max_length=128, null=False,
                            blank=False, unique=True)
    descricao = models.TextField(blank=True)
    usuario = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


# Lista: lista de atividades

class Lista(models.Model):
    nome = models.CharField(max_length=128, null=False,
                            blank=False)
    projeto = models.ForeignKey(Projeto, on_delete=models.CASCADE)
    OPC = (
        ('pendente', 'Pendente'),
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    )
    status = models.CharField(max_length=8, null=True,
                              choices=OPC, default=OPC[0][0])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['projeto', 'nome'], name='unica_lista')
        ]

# Atividade


class Atividade(models.Model):
    titulo = models.CharField(max_length=128, null=False,
                              blank=False)
    descricao = models.TextField(blank=True)
    membros = models.ManyToManyField(User, blank=True)
    # etiqueta = models.CharField(max_length=255)
    # = models.DateTimeField()
    OPC = (
        ('pendente', 'Pendente'),
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    )
    status = models.CharField(max_length=8, null=True,
                              choices=OPC, default=OPC[0][0])
    requisitos = models.ManyToManyField('Atividade', blank=True)
    lista = models.ForeignKey(Lista, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['titulo', 'lista'], name='unica_atv')
        ]


'''

class Itens(models.Model):
    titulo = models.CharField(max_length=128, null=False,
                              blank=False, unique=True)
    OPC = (
        ('pendente', 'Pendente'),
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    )
    status = models.CharField(max_length=8, null=True,
                              choices=OPC, default=OPC[0][0])
    requisitos = models.ManyToManyField('Itens', blank=True)
    atividade = models.ForeignKey(Atividade, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
'''
