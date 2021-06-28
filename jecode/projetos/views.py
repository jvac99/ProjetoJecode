from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import *
from .forms import *

# Primeira tela, antes do login e do cadastro.


def index(request):
    return render(request, 'index.html')

# Primeira tela, depois do login.


@login_required
def inicio(request):
    projetos = listar_projetos(request)
    return render(request, 'projetos/inicio.html', {'projetos': projetos})


@login_required
def novo_projeto(request):
    # projetos = Projeto.objects.all().order_by(
    #    '-created_at').filter(usuario=request.user)
    if request.method == 'POST':
        form = ProjetoForm(request.POST)

        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            messages.info(request, 'Projeto salvo com sucesso.')
            # return redirect('../listar_projetos')
    else:
        form = ProjetoForm()
        # return render(request, 'projetos/listar_projetos.html', {'projetos': projetos, 'form': form})
    return form


@login_required
def listar_projetos(request):
    return Projeto.objects.all().order_by(
        '-created_at').filter(usuario=request.user)


'''
@login_required
def listas_de_projetos(request):
    projetos = Projeto.objects.all().order_by(
        '-created_at').filter(usuario=request.user)
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            return redirect('../listar_projetos')
    else:
        form = ProjetoForm()
        return render(request, 'projetos/listar_projetos.html', {'projetos': projetos, 'form': form})
'''


@login_required
def listas_de_projetos(request):
    projetos = listar_projetos(request)
    form = novo_projeto(request)
    return render(request, 'projetos/listar_projetos.html', {'projetos': projetos, 'form': form})


@login_required
def editar_projeto(request, id):
    pass


@login_required
def deletar_projeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    projeto.delete()
    messages.info(request, 'Projeto deletado com sucesso.')
    return redirect('listar_projetos')


def listar_listas_projeto(projeto):
    return Lista.objects.all().filter(projeto=projeto)


@login_required
def detalhes_do_projeto(request, id):
    projetos = listar_projetos(request)
    projeto = get_object_or_404(Projeto, pk=id)
    listas = listar_listas_projeto(projeto)
    atividades = listar_atividades_do_projeto()
    form_lista = nova_lista_do_projeto(request)
    form_atividade = nova_atividade_do_projeto(request)
    #atividades = listar_atividades_do_projeto(projeto)
    '''
     if request.method == 'POST':
        form_lista = ListaForm(request.POST)
        form_atividade = AtividadeForm(request.POST)
        if form_lista.is_valid():
            lista = form_lista.save(commit=False)
            lista.projeto = projeto
            lista.save()
            return render(request, 'projetos/detalhes_do_projeto.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista})
        if form_atividade.is_valid():
            atividade = form_atividade.save(commit=False)
            # atividade.lista = lista
            # lista.save()
            return render(request, 'projetos/detalhes_do_projeto.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista})
    else:
        form_lista = ListaForm()
        return render(request, 'projetos/detalhes_do_projeto.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista})
    '''
    return render(request, 'projetos/detalhes_do_projeto.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista, 'form_atividade': form_atividade})


@login_required
def nova_lista_do_projeto(request):
    if request.method == 'POST':
        form = ListaForm(request.POST)

        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            # return redirect('../projetos_lista')
    else:
        form = ListaForm()
        # return render(request, 'projetos/listar_projetos.html', {'projetos': projetos, 'form': form})
    return form


@login_required
def lista_de_listas_do_projeto(request, id):
    pass


@login_required
def editar_lista_do_projeto(request, id):
    pass


@login_required
def deletar_lista_do_projeto(request, id):
    lista = get_object_or_404(Lista, pk=id)
    lista.delete()
    messages.info(request, 'Lista deletada com sucesso.')
    return redirect('../listar_projetos')


@login_required
def detalhes_da_atividade_do_projeto(request, id):
    pass


@login_required
def nova_atividade_do_projeto(request):
    # projetos = Projeto.objects.all().order_by(
    #    '-created_at').filter(usuario=request.user)
    if request.method == 'POST':
        form = AtividadeForm(request.POST)

        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            return redirect('../projetos_lista')
    else:
        form = AtividadeForm()
        # return render(request, 'projetos/listar_projetos.html', {'projetos': projetos, 'form': form})
    return form

@login_required
def lista_de_atividades_do_projeto(request, id):
    pass


def listar_atividades_do_projeto():
    return Atividade.objects.all()


@login_required
def editar_atividade_do_projeto(request, id):
    pass


@login_required
def deletar_atividade_do_projeto(request, id):
    atividade = get_object_or_404(Atividade, pk=id)
    atividade.delete()
    messages.info(request, 'Atividade deletada com sucesso.')
    return redirect('../detalhes_da_atividade')
