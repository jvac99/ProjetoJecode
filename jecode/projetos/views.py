from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import *
from .forms import *


def index(request):
    return render(request, 'index.html')


@login_required
def login(request):
    return render(request, 'projetos/login.html')


@login_required
def cadastro(request):
    return render(request, 'projetos/cadastro.html')


@login_required
def inicio(request):
    projetos = Projeto.objects.all().order_by(
        '-created_at').filter(usuario=request.user)
    return render(request, 'projetos/inicio.html', {'projetos': projetos})


@login_required
def projetos_lista(request):
    projetos = Projeto.objects.all().order_by(
        '-created_at').filter(usuario=request.user)
    if request.method == 'POST':
        form = ProjetoForm(request.POST)
        if form.is_valid():
            projeto = form.save(commit=False)
            projeto.usuario = request.user
            projeto.save()
            return redirect('../projetos_lista')
    else:
        form = ProjetoForm()
        return render(request, 'projetos/projetos_lista.html', {'projetos': projetos, 'form': form})


@login_required
def projeto_detalhes(request, id):
    projetos = Projeto.objects.all().order_by(
        '-created_at').filter(usuario=request.user)
    projeto = get_object_or_404(Projeto, pk=id)
    listas = Lista.objects.all().filter(projeto=projeto)
    atividades = Atividade.objects.all()
    if request.method == 'POST':
        form_lista = ListaForm(request.POST)
        form_atividade = AtividadeForm(request.POST)
        if form_lista.is_valid():
            lista = form_lista.save(commit=False)
            lista.projeto = projeto
            lista.save()
            return render(request, 'projetos/projeto_detalhes.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista})
        if form_atividade.is_valid():
            atividade = form_atividade.save(commit=False)
            atividade.lista = lista
            # lista.save()
            return render(request, 'projetos/projeto_detalhes.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista})
    else:
        form_lista = ListaForm()
        return render(request, 'projetos/projeto_detalhes.html', {'projeto': projeto, 'projetos': projetos, 'listas': listas, 'atividades': atividades, 'form_lista': form_lista})


@login_required
def deleteProjeto(request, id):
    projeto = get_object_or_404(Projeto, pk=id)
    projeto.delete()
    # messages.info(request, 'Tarefa deletada com sucesso.')
    return redirect('../projetos_lista')
