from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import AlunoForm, Aluno, LoginForm

def cadastrar_aluno(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            form.save()  # Salva o novo aluno no banco de dados
            return redirect('lista_alunos')  # Redireciona para a página de lista de alunos
    else:
        form = AlunoForm()

    return render(request, 'app_escola/cadastrar_aluno.html', {'form': form})

def lista_alunos(request):
    alunos = Aluno.objects.all()  # Pega todos os alunos cadastrados no banco
    return render(request, 'app_escola/lista_alunos.html', {'alunos': alunos})




def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('lista_alunos')  # Redirecionar para a página de lista de alunos após o login
            else:
                form.add_error(None, "Email ou senha incorretos")
    else:
        form = LoginForm()

    return render(request, 'app_escola/login.html', {'form': form})


def home(request):
    return render(request, 'app_escola/home.html')

def agendamento_view(request):
    return render(request, 'app_escola/agendamento.html')

def diario_turma_view(request):
    return render(request, 'app_escola/diario_turma.html')

def faltas_view(request):
    return render(request, 'app_escola/faltas.html')

def cadastrar_aluno_view(request):
    return render(request, 'app_escola/cadastrar_aluno.html')

def logout_view(request):
    return redirect('login')
