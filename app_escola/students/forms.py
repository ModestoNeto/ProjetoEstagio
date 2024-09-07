from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    """Formulário para o cadastro de alunos."""
    class Meta:
        model = Student
        fields = ['name', 'cpf', 'address']
