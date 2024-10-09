# app_escola/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required  # Decorator para proteger views

# Página inicial (disponível apenas para usuários logados)
@login_required
def home(request):
    return render(request, 'app_escola/home.html')

# Página de cadastro de aluno (disponível apenas para superusuários)
@login_required
def cadastrar_aluno(request):
    if not request.user.is_superuser:  # Verifica se o usuário é um superusuário
        return redirect('home')  # Redireciona para a home se não for superusuário
    return render(request, 'app_escola/cadastrar_aluno.html')

# Lista de alunos (disponível apenas para superusuários)
@login_required
def lista_alunos(request):
    if not request.user.is_superuser:  # Verifica se o usuário é um superusuário
        return redirect('home')
    return render(request, 'app_escola/lista_alunos.html')

# Página de agendamento (disponível apenas para usuários logados)
@login_required
def agendamento(request):
    return render(request, 'app_escola/agendamento.html')

# Diário de turma (disponível apenas para usuários logados)
@login_required
def diario_turma(request):
    return render(request, 'app_escola/diario_turma.html')

# Controle de faltas (disponível apenas para usuários logados)
@login_required
def faltas(request):
    return render(request, 'app_escola/faltas.html')
