from django.db import models
from django.contrib.auth.models import User
from .utils.simple_crypto import encrypt, decrypt

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    email = models.EmailField()
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=255, unique=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    serie = models.CharField(max_length=10, null=True)
    turma = models.CharField(max_length=10, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nome

    # Criptografando o CPF antes de salvar
    def save(self, *args, **kwargs):
        if self.cpf:
            self.cpf = encrypt(self.cpf)  # Criptografando o CPF antes de salvar
        super().save(*args, **kwargs)

    # Função para descriptografar o CPF ao acessar
    @property
    def decrypted_cpf(self):
        return decrypt(self.cpf)  # Descriptografando o CPF ao acessar
