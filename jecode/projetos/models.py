from django.db import models
from django.contrib.auth.models import User

# Projeto: contém o projeto.


class Projeto(models.Model):
    # Nome: nome do projeto.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )
    # Descricao: Descrição do projeto.
    descricao = models.TextField(
        blank=True
    )
    # Usuario: criador do Projeto (chave estrangeira).
    usuario = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Projetos'

        ordering = ('created_at',)

    def __str__(self):
        return self.nome


# Lista: contém as lista de atividades do projeto.

class Lista(models.Model):
    # Nome: nome da lista.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )
    # Projeto: Projeto da qual a lista pertence (chave estrangeira).
    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE
    )
    # OPC = contém as opções dos quais os status da lista poderá assumir (tupla de tuplas = choices).
    OPC = (
        ('pendente', 'Pendente'),
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    )
    # Status = é uma das opções de OPC, inicia com a opção 0.
    status = models.CharField(
        max_length=8,
        null=True,
        choices=OPC,
        default=OPC[0][0]
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Listas'

        ordering = ('created_at',)

        constraints = [
            models.UniqueConstraint(
                fields=['projeto', 'nome'],
                name='unica_lista'
            )
        ]

    def __str__(self):
        return self.nome

# Atividade: contém as atividades da lista.


class Atividade(models.Model):
    # Titulo: título da atividade.
    titulo = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )
    # Descricao: descrição das atividades.
    descricao = models.TextField(
        blank=True
    )
    # Membros: contém os membros que farão a atividade.
    membros = models.ManyToManyField(
        User,
        blank=True
    )

    # etiqueta = models.CharField(max_length=255)
    # = models.DateTimeField()

    # OPC = contém as opções dos quais os status da lista poderá assumir (tupla de tuplas = choices).
    OPC = (
        ('pendente', 'Pendente'),
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    )
    # Status = é uma das opções de OPC, inicia com a opção 0.
    status = models.CharField(
        max_length=8,
        null=True,
        choices=OPC,
        default=OPC[0][0]
    )

    lista = models.ForeignKey(
        Lista,
        on_delete=models.CASCADE
    )
    # Requsitos = são os requisitos necessários para que a atividade seja iniciada.
    requisitos = models.ManyToManyField(
        'self',
        blank=True,
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Atividades'

        ordering = ('created_at',)

        constraints = [
            models.UniqueConstraint(
                fields=['titulo', 'lista'],
                name='unica_atv'
            )
        ]

    def __str__(self):
        return self.titulo


class Subatividade(models.Model):

    titulo = models.CharField(
        max_length=128,
        null=False,
        blank=False
    )

    descricao = models.TextField(
        blank=True
    )

    OPC = (
        ('pendente', 'Pendente'),
        ('fazendo', 'Fazendo'),
        ('feito', 'Feito'),
    )

    status = models.CharField(
        max_length=8,
        null=True,
        choices=OPC,
        default=OPC[0][0]
    )

    atividade = models.ForeignKey(
        Atividade,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name_plural = 'Subatividades'

        ordering = ('created_at',)

        constraints = [
            models.UniqueConstraint(
                fields=['titulo', 'atividade'],
                name='unica_subatv'
            )
        ]

    def __str__(self):
        return self.titulo
