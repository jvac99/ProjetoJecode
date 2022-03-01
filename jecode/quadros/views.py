from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import *
from .models import *

# Método para listar todos os quadros.


@login_required
def listar_quadros(request):
    return Quadro.objects.all().order_by(
        '-created_at').filter(usuario=request.user)

# Primeira tela.


def index(request):
    quadros = listar_quadros(request)  # carregando os quadros
    return render(request, 'quadros/index.html', {'quadros': quadros})

# -------- Quadros ---------

# Tela que contém a lista dos quadros e um botão de adicionar novo quadro.


@login_required
def quadros(request):
    quadros = listar_quadros(request)
    return render(request, 'quadros/quadros.html', {'quadros': quadros})


@login_required
def quadro(request, id_quadro):
    try:
        quadro = get_object_or_404(Quadro, pk=id_quadro)
    except:
        redirect('/home')
    quadros = listar_quadros(request)  # carregando os quadros
    return render(request, 'quadros/quadro.html', {'quadros': quadros, 'quadro': quadro})

# Adicionando um novo quadro.


@login_required
def novo_quadro(request):
    if request.method == 'POST':
        form = QuadroForm(request.POST)
        if form.is_valid():
            quadro = form.save(commit=False)
            quadro.usuario = request.user
            quadro.save()
            messages.info(request, 'Quadro salvo com sucesso.')
            return redirect('/quadros/')
        else:
            return render(request, 'quadros/novo_quadro.html', {'form': form})
    else:
        form = QuadroForm()
        return render(request, 'quadros/novo_quadro.html', {'quadros': quadros, 'form': form})

# Editar quadro


@login_required
def editar_quadro(request, id):
    quadro = get_object_or_404(Quadro, pk=id)
    if request.method == 'POST':
        form = QuadroForm(request.POST, instance=quadro)
        if form.is_valid():
            quadro = form.save(commit=False)
            quadro.usuario = request.user
            quadro.save()
            messages.info(request, 'Quadro salvo com sucesso.')
            return redirect('/quadros/')
        else:
            return render(request, 'quadros/editar_quadro.html', {'form': form})
    else:
        form = QuadroForm(instance=quadro)
        return render(request, 'quadros/editar_quadro.html', {'form': form})

# Deletar quadro


@login_required
def deletar_quadro(request, id):
    quadro = get_object_or_404(Quadro, pk=id)  # Buscando o quadro
    quadro.delete()  # Deletando o quadro
    messages.info(request, 'Quadro deletado com sucesso.')
    return redirect('/quadros/')
