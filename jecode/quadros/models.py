from django.db import models
from django.contrib.auth.models import User


# Quadro: contém o quadro.


class Quadro(models.Model):
    # Nome: nome do quadro.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )
    # Descricao: Descrição do quadro.
    descricao = models.TextField(
        blank=True
    )
    # Usuario: criador do Quadro (chave estrangeira).
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

        verbose_name_plural = 'Quadros'
        ordering = ('created_at',)

    def __str__(self):
        return self.nome


# Coluna: contém as colunas.


class Coluna(models.Model):
    # Nome: nome da coluna.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )

    # Quadro: quadro que a coluna pertence (chave estrangeira).
    quadro = models.ForeignKey(
        Quadro,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Colunas'

        ordering = ('created_at',)

    def __str__(self):
        return self.nome

# Linha: contém as linhas.


class Linha(models.Model):
    # Nome: nome da linha.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )

    # Quadro: quadro que a linha pertence (chave estrangeira).
    quadro = models.ForeignKey(
        Quadro,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Linhas'

        ordering = ('created_at',)

    def __str__(self):
        return self.nome


# Status: contém os status.


class Status(models.Model):
    # Nome: nome da linha.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )

    # Quadro: quadro que a coluna pertence (chave estrangeira).
    quadro = models.ForeignKey(
        Quadro,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Status'

        ordering = ('created_at',)

    def __str__(self):
        return self.nome


# Tipo: contém os status.


class Tipo(models.Model):
    # Nome: nome da linha.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )

    # Quadro: quadro que a coluna pertence (chave estrangeira).
    quadro = models.ForeignKey(
        Quadro,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Tipos'

        ordering = ('created_at',)

    def __str__(self):
        return self.nome


# Epico: contém o epico.


class Epico(models.Model):
    # Nome: nome do epico.
    nome = models.CharField(
        max_length=128,
        null=False,
        blank=False,
        unique=True
    )
    # Descricao: Descrição do epico.
    descricao = models.TextField(
        blank=True
    )
    # Quadro: quadro que o epico pertence (chave estrangeira).
    quadro = models.ForeignKey(
        Quadro,
        on_delete=models.PROTECT
    )

    # Status: status  do epico (chave estrangeira).
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:

        verbose_name_plural = 'Epicos'

        ordering = ('created_at',)

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

    linha = models.ForeignKey(
        Linha,
        on_delete=models.PROTECT
    )

    coluna = models.ForeignKey(
        Coluna,
        on_delete=models.PROTECT
    )

    # Status: status  da atividade (chave estrangeira).
    status = models.ForeignKey(
        Status,
        on_delete=models.PROTECT
    )

    # Tipo: tipo da atividade (chave estrangeira).
    tipo = models.ForeignKey(
        Tipo,
        on_delete=models.PROTECT
    )

    # Epico: epico da atividade (chave estrangeira).
    epico = models.ForeignKey(
        Epico,
        on_delete=models.PROTECT
    )

    data_de_inicio = models.DateTimeField(
        auto_now_add=True
    )

    data_de_entrega = models.DateTimeField(
        null=False,
        blank=False
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

    def __str__(self):
        return self.titulo
