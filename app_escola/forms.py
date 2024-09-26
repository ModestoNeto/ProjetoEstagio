from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    cpf = forms.CharField(max_length=11)  # O CPF será fornecido pelo usuário no cadastro

    class Meta:
        model = Aluno
        fields = ['nome', 'cpf', 'telefone', 'endereco', 'genero']

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Senha")
