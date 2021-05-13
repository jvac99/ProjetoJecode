from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Projeto

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
    projetos = Projeto.objects.all()
    return render(request, 'projetos/inicio.html', {'projetos': projetos})


@login_required
def projetos_lista(request):
    projetos = Projeto.objects.all()
    return render(request, 'projetos/projetos_lista.html', {'projetos': projetos})


@login_required
def projeto_detalhes(request, id):
    projetos = Projeto.objects.all()
    projeto = get_object_or_404(Projeto, pk=id)
    return render(request, 'projetos/projeto_detalhes.html', {'projeto': projeto, 'projetos': projetos})
