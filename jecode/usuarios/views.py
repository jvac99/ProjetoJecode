from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required

@require_POST
def login(request):
    usuario_aux = User.objects.get(email=request.POST['email'])
    usuario = authenticate(username=usuario_aux.username,
                           password=request.POST["senha"])
    if usuario is not None:
        login(request, usuario)
        return HttpResponseRedirect('/index/')

    return HttpResponseRedirect('/')

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect('/')

@require_POST
def cadastro(request):
    try:
        usuario_email = User.objects.get(email=request.POST['campo-email'])
        usuario_username = User.objects.get(
            email=request.POST['campo-nome-usuario'])

        if usuario_email or usuario_username:
            return render(request, 'caminho para o index', {'msg': 'Erro! Já existe um usuário com o mesmo e-mail ou mesmo username'})

    except User.DoesNotExist:
        nome_usuario = request.POST['campo-nome-usuario']
        email = request.POST['campo-email']
        senha = request.POST['campo-senha']

        novoUsuario = User.objects.create_user(
            username=nome_usuario, email=email, password=senha)
        novoUsuario.save()