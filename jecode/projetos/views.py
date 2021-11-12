from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *
from django.db import IntegrityError


# Métodos

# Método para listando todos os projetos.

@login_required
def listar_projetos(request):
    return Projeto.objects.all().order_by(
        '-created_at').filter(usuario=request.user)

# Primeira tela, antes do login e do cadastro.


def index(request):
    projetos = listar_projetos(request)  # carregando os projetos
    return render(request, 'index.html', {'projetos': projetos})

# Primeira tela, depois do login.


@login_required
def inicio(request):
    projetos = listar_projetos(request)  # carregando os projetos
    return render(request, 'projetos/inicio.html', {'projetos': projetos})

# Adicionando um novo projeto.


@login_required
def novo_projeto(request):
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            messages.info(request, 'Projeto salvo com sucesso.')
    return ProjetoForm()

# Tela que contém a lista dos projetos e um uma função de adicionar.


@login_required
def listas_de_projetos(request):
    projetos = listar_projetos(request)
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            messages.info(request, 'Projeto salvo com sucesso.')
            return redirect('/listas_de_projetos/')
        else:
            return render(request, 'projetos/lista_de_projetos.html', {'projetos': projetos, 'form': form})
    else:
        form = ProjetoForm()
        return render(request, 'projetos/lista_de_projetos.html', {'projetos': projetos, 'form': form})

# Editar projeto


@login_required
def editar_projeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    projetos = listar_projetos(request)
    if request.method == 'POST':
        form = ProjetoForm(request.POST, instance=projeto)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            messages.info(request, 'Projeto salvo com sucesso.')
            return redirect('/listas_de_projetos/')
        else:
            return render(request, 'projetos/editar_projeto.html', {'projetos': projetos, 'form': form})
    else:
        form = ProjetoForm(instance=projeto)
        return render(request, 'projetos/editar_projeto.html', {'projetos': projetos, 'form': form})

# Deletar projeto


@login_required
def deletar_projeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)  # Buscando o projeto
    projeto.delete()  # Deletando o projeto
    messages.info(request, 'Projeto deletado com sucesso.')
    return redirect('/listas_de_projetos/')

# Listas do Projetos


def listar_listas_projeto(projeto):
    return Lista.objects.all().filter(projeto=projeto)

# Detalhes do projeto tem todas as listas do projeto, estás lista contém as atividades.


@login_required
def detalhes_do_projeto(request, id_projeto):
    projetos = listar_projetos(request)
    projeto = get_object_or_404(Projeto, pk=id_projeto)
    listas = listar_listas_projeto(projeto)
    atividades = listar_atividades_do_projeto()
    if request.method == 'POST':
        form_lista = ListaForm(request.POST)
        form_atividade = AtividadeForm(request.POST)
        if form_lista.is_valid():
            try:
                lista = form_lista.save(commit=False)
                lista.projeto = projeto
                lista.save()
                messages.info(request, 'Lista salva com sucesso.')
                return redirect('/detalhes_do_projeto/{id}'.format(id=id_projeto))
            except IntegrityError as e:
                messages.error(
                    request, 'Error já existe uma lista com este nome.')
                return render(request, 'projetos/detalhes_do_projeto.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista, 'form_atividade': form_atividade})
        else:
            return render(request, 'projetos/detalhes_do_projeto.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista, 'form_atividade': form_atividade})
    else:
        form_lista = ListaForm()
        form_atividade = AtividadeForm()
        return render(request, 'projetos/detalhes_do_projeto.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista, 'form_atividade': form_atividade})


@login_required
def nova_lista_do_projeto(request, projeto):
    if request.method == 'POST':
        form = ListaForm(request.POST)

        if form.is_valid():
            lista = form.save(commit=False)
            lista.projeto = projeto
            lista.save()
            return redirect('/detalhes_do_projeto/{id}'.format(id=id))
    else:
        form = ListaForm()
        return redirect('/detalhes_do_projeto/{id}'.format(id=id))
    return form


@login_required
def lista_de_listas_do_projeto(request, id):
    pass


@login_required
def detalhes_da_lista_do_projeto(request, id):
    projetos = listar_projetos(request)
    lista = get_object_or_404(Lista, pk=id)
    atividades = Atividade.objects.all().filter(lista=lista)
    pendentes = []
    fazendo = []
    feito = []
    for atv in atividades:
        if atv.status == "pendente" or atv.status == "Pendente":
            pendentes.append(atv)
        elif atv.status == "fazendo" or atv.status == "Fazendo":
            fazendo.append(atv)
        elif atv.status == "feito" or atv.status == "Feito":
            feito.append(atv)
    return render(request, 'projetos/detalhes_da_lista.html', {'lista': lista, 'pendentes': pendentes, 'fazendo': fazendo, 'feito': feito,  'projetos': projetos})


@login_required
def editar_lista_do_projeto(request, id):
    pass


@login_required
def deletar_lista_do_projeto(request, id_lista, id_projeto):
    lista = get_object_or_404(Lista, pk=id_lista)
    lista.delete()
    messages.info(request, 'Lista deletada com sucesso.')
    return redirect('/detalhes_do_projeto/{id}'.format(id=id_projeto))


@login_required
def detalhes_da_atividade_do_projeto(request, id):
    atividade = get_object_or_404(Atividade, pk=id)
    subatividades = Subatividade.objects.all().filter(atividade=atividade)
    projetos = listar_projetos(request)
    pendentes = []
    fazendo = []
    feito = []
    for atv in subatividades:
        if atv.status == "pendente" or atv.status == "Pendente":
            pendentes.append(atv)
        elif atv.status == "fazendo" or atv.status == "Fazendo":
            fazendo.append(atv)
        elif atv.status == "feito" or atv.status == "Feito":
            feito.append(atv)
    projetos = listar_projetos(request)
    return render(request, 'projetos/detalhes_da_atividade.html', {'projetos': projetos, 'atividade': atividade, 'pendentes': pendentes, 'fazendo': fazendo, 'feito': feito})


@login_required
def nova_atividade_do_projeto(request, id_lista, prox):
    projetos = listar_projetos(request)
    lista = get_object_or_404(Lista, pk=id_lista)
    if request.method == 'POST':
        form_atividade = AtividadeForm(request.POST)
        if form_atividade.is_valid():
            try:
                atividade = form_atividade.save(commit=False)
                atividade.lista = lista
                atividade.save()
                endereco = '/detalhes_do_projeto/{id}'.format(
                    id=lista.projeto.id) if prox else '/detalhes_da_lista_do_projeto/{id}'.format(id=lista.id)
                return redirect(endereco)
            except IntegrityError as e:
                messages.error(
                    request, 'Error já existe uma atividade com este titulo.')
                return render(request, 'projetos/nova_atividade.html', {'form_atividade': form_atividade, 'projetos': projetos})
        else:
            return render(request, 'projetos/nova_atividade.html', {'form_atividade': form_atividade, 'projetos': projetos})
    else:
        form_atividade = AtividadeForm()
        return render(request, 'projetos/nova_atividade.html', {'form_atividade': form_atividade, 'projetos': projetos})


@login_required
def lista_de_atividades_do_projeto(request, id):
    pass


@login_required
def mudar_estado_da_atividades_do_projeto(request, id, dir):
    atv = get_object_or_404(Atividade, pk=id)

    if atv.status == "pendente" or atv.status == "Pendente":
        if atv.requisitos:
            atv.status = "fazendo"
    elif (atv.status == "fazendo" or atv.status == "Fazendo"):
        if dir:
            atv.status = "feito"
        else:
            atv.status = "pendente"
    else:
        atv.status = "fazendo"
    atv.save()
    return redirect('/detalhes_da_lista_do_projeto/{id}'.format(id=atv.lista.id))


def listar_atividades_do_projeto():
    return Atividade.objects.all()


@login_required
def editar_atividade_do_projeto(request, id):
    atividade = get_object_or_404(Atividade, pk=id)
    if request.method == 'POST':
        form_atividadeEditar = AtividadeFormEditar(
            request.POST, instance=atividade)
        if form_atividadeEditar.is_valid():
            try:
                atividade = form_atividadeEditar.save(commit=False)
                atividade.save()
                return redirect('/detalhes_do_projeto/{id}'.format(id=atividade.lista.projeto.id))
            except IntegrityError as e:
                return render(request, 'projetos/editar_atividade.html', {'form_atividadeEditar': form_atividadeEditar})
        else:
            return render(request, 'projetos/editar_atividade.html', {'form_atividadeEditar': form_atividadeEditar})
    else:
        form_atividadeEditar = AtividadeFormEditar(instance=atividade)
        return render(request, 'projetos/editar_atividade.html', {'form_atividadeEditar': form_atividadeEditar})


# Deleta uma atividade de uma lista do projeto

@login_required
def deletar_atividade_do_projeto(request, id):
    atividade = get_object_or_404(Atividade, pk=id)  # Buscando a atividade
    lista = atividade.lista
    atividade.delete()
    messages.info(request, 'Atividade deletada com sucesso.')
    return redirect('/detalhes_do_projeto/{id}'.format(id=lista.projeto.id))


@login_required
def nova_subatividade_do_projeto(request, id_atividade):
    projetos = listar_projetos(request)
    atividade = get_object_or_404(Atividade, pk=id_atividade)
    if request.method == 'POST':
        form_subatividade = SubatividadeForm(request.POST)
        if form_subatividade.is_valid():
            try:
                subatividade = form_subatividade.save(commit=False)
                subatividade.atividade = atividade
                subatividade.save()
                return redirect('/detalhes_da_atividade_do_projeto/{id}'.format(id=atividade.id))
            except IntegrityError as e:
                messages.error(
                    request, 'Error já existe uma subatividade com este titulo.')
                return render(request, 'projetos/nova_subatividade.html', {'form_subatividade': form_subatividade, 'projetos': projetos})
        else:
            return render(request, 'projetos/nova_subatividade.html', {'form_subatividade': form_subatividade, 'projetos': projetos})
    else:
        form_subatividade = SubatividadeForm()
        return render(request, 'projetos/nova_subatividade.html', {'form_subatividade': form_subatividade, 'projetos': projetos})


@login_required
def mudar_estado_da_subatividades_do_projeto(request, id, dir):
    subatv = get_object_or_404(Subatividade, pk=id)

    if subatv.status == "pendente" or subatv.status == "Pendente":
        subatv.status = "fazendo"
    elif (subatv.status == "fazendo" or subatv.status == "Fazendo"):
        if dir:
            subatv.status = "feito"
        else:
            subatv.status = "pendente"
    else:
        subatv.status = "fazendo"
    subatv.save()
    return redirect('/detalhes_da_atividade_do_projeto/{id}'.format(id=subatv.atividade.id))


def listar_subatividades_do_projeto():
    return Subatividade.objects.all()


@login_required
def editar_subatividade_do_projeto(request, id):
    subatividade = get_object_or_404(Subatividade, pk=id)
    if request.method == 'POST':
        form_subatividadeEditar = SubatividadeFormEditar(
            request.POST, instance=subatividade)
        if form_subatividadeEditar.is_valid():
            try:
                subatividade = form_subatividadeEditar.save(commit=False)
                subatividade.save()
                return redirect('/detalhes_da_atividade_do_projeto/{id}'.format(id=subatividade.atividade.id))
            except IntegrityError as e:
                return render(request, 'projetos/editar_subatividade.html', {'form_subatividadeEditar': form_subatividadeEditar})
        else:
            return render(request, 'projetos/editar_subatividade.html', {'form_subatividadeEditar': form_subatividadeEditar})
    else:
        form_subatividadeEditar = SubatividadeFormEditar(instance=subatividade)
        return render(request, 'projetos/editar_subatividade.html', {'form_subatividadeEditar': form_subatividadeEditar})


# Deleta uma atividade de uma lista do projeto

@login_required
def deletar_subatividade_do_projeto(request, id):
    subatividade = get_object_or_404(
        Subatividade, pk=id)  # Buscando a subatividade
    atividade = subatividade.atividade
    subatividade.delete()
    messages.info(request, 'subatividade deletada com sucesso.')
    return redirect('/detalhes_da_atividade_do_projeto/{id}'.format(id=atividade.id))
