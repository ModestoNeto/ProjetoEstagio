from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    cpf = forms.CharField(max_length=11)  # O CPF será fornecido pelo usuário

    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'telefone', 'endereco', 'genero']
