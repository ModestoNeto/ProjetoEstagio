from .models import Aluno
from .forms import AlunoForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils.simple_crypto import decrypt

@login_required
def alunoView(request):
    alunos_list = Aluno.objects.all()
    
    alunos_with_decrypted_cpf = []
    for aluno in alunos_list:
        aluno_cpf = decrypt(aluno.cpf)  # Descriptografando o CPF
        alunos_with_decrypted_cpf.append({
            'aluno': aluno,
            'decrypted_cpf': aluno_cpf
        })
    
    return render(request, 'main/alunos.html', {'alunos_list': alunos_with_decrypted_cpf})

@login_required
def alunoIDview(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    aluno_cpf = aluno.decrypted_cpf 

    return render(request, 'main/alunoID.html', {'aluno': aluno, 'aluno_cpf': aluno_cpf})

@login_required
def criarAlunoView(request):
    if request.method == 'POST':
        form = AlunoForm(request.POST)
        if form.is_valid():
            aluno = form.save(commit=False)
            aluno.user = request.user
            aluno.save()
            messages.success(request, "Aluno criado com sucesso!")
            return redirect('aluno_view')
    else:
        form = AlunoForm()

    return render(request, 'main/criar_aluno.html', {'form': form})

@login_required
def atualizarAlunoView(request, id):
    aluno = get_object_or_404(Aluno, pk=id)
    
    if request.method == 'POST':
        form = AlunoForm(request.POST, instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request, "Aluno atualizado com sucesso!")
            return redirect('aluno_view')
    else:
        form = AlunoForm(instance=aluno)

    return render(request, 'main/criar_aluno.html', {'form': form})
