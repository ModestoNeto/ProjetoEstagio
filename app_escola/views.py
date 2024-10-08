from django.shortcuts import render, redirect
from .forms import AlunoForm
from .models import Aluno

# View para cadastrar um aluno e tokenizar o CPF
def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.save()  # O CPF será salvo como um token
            return redirect('lista_alunos')
    else:
        form = AlunoForm()
    return render(request, 'app_escola/cadastrar_aluno.html', {'form': form})

# View para listar todos os alunos e descriptografar o CPF para exibição
def lista_alunos(request):
    alunos = Aluno.objects.all()
    for aluno in alunos:
        aluno.cpf_decrypted = aluno.get_decrypted_cpf()  # Recupera o CPF descriptografado
    return render(request, 'app_escola/lista_alunos.html', {'alunos': alunos})

# View para exibir a página inicial
def home(request):
    return render(request, 'app_escola/home.html')  # Ajustado para o caminho correto do template

# View para gerenciar o login do usuário
def login_view(request):
    return render(request, 'app_escola/login.html')  # Ajustado para o caminho correto do template

# View para exibir a página de agendamento de eventos
def agendamento_view(request):
    return render(request, 'app_escola/agendamento.html')  # Ajustado para o caminho correto do template

# View para exibir a página de diário de turma
def diario_turma_view(request):
    return render(request, 'app_escola/diario_turma.html')  # Ajustado para o caminho correto do template

# View para exibir a página de controle de faltas
def faltas_view(request):
    return render(request, 'app_escola/faltas.html')  # Ajustado para o caminho correto do template

# View para gerenciar o logout do usuário
def logout_view(request):
    return redirect('home')
