from django.shortcuts import render

# View para a página inicial
def home(request):
    return render(request, 'app_escola/home.html')

# View para a página de perfil do usuário
def perfil(request):
    return render(request, 'app_escola/perfil.html')

# View para a página de cadastro de aluno
def cadastrar_aluno(request):
    return render(request, 'app_escola/cadastrar_aluno.html')

# View para a lista de alunos
def lista_alunos(request):
    return render(request, 'app_escola/lista_alunos.html')

# View para a página de agendamento
def agendamento(request):
    return render(request, 'app_escola/agendamento.html')

# View para a página de diário de turma
def diario_turma(request):
    return render(request, 'app_escola/diario_turma.html')

