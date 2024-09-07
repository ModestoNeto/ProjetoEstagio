from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student

def register_student(request):
    """View para exibir o formulário de cadastro e processar os dados."""
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'students/register_student.html', {'form': form})

def student_list(request):
    """View para listar todos os alunos cadastrados."""
    students = Student.objects.all()
    return render(request, 'students/student_list.html', {'students': students})
