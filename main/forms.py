from django import forms
from .models import Aluno

class AlunoForm(forms.ModelForm):
    telefone = forms.CharField(widget=forms.TextInput(attrs={'minlength': '15', 'maxlength': '15', 'onkeyup': 'handlePhone(event)'}))
    data_nascimento = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    cpf = forms.CharField(widget=forms.TextInput(attrs={'maxlength': '14', 'oninput': 'handleCPF(event)'}))
    class Meta:
        model = Aluno
        fields = ['nome', 'telefone', 'email', 'data_nascimento', 'cpf', 'serie', 'turma', 'description']
    
    description = forms.CharField(required=False, widget=forms.Textarea)


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['nome'].widget.attrs.update({'class': 'form-control'})
        self.fields['telefone'].widget.attrs.update({'class': 'form-control'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['data_nascimento'].widget.attrs.update({'class': 'form-control'})
        self.fields['cpf'].widget.attrs.update({'class': 'form-control'})
        self.fields['description'].widget.attrs.update({'class': 'form-control'})
        self.fields['serie'].widget.attrs.update({'class': 'form-control'})
        self.fields['turma'].widget.attrs.update({'class': 'form-control'})
