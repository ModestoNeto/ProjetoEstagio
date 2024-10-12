from django.db import models
from cryptography.fernet import Fernet
import base64

# Gerar a chave de criptografia (deve ser armazenada em segurança)
KEY = Fernet.generate_key()
cipher_suite = Fernet(KEY)

class Aluno(models.Model):
    nome = models.CharField(max_length=255)
    cpf_token = models.CharField(max_length=255, unique=True, editable=False)  # CPF armazenado como token
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    genero = models.CharField(max_length=10)

    def save(self, *args, **kwargs):
        # Criptografar o CPF antes de salvar no banco de dados
        if not self.cpf_token:
            cpf_encrypted = cipher_suite.encrypt(self.cpf.encode('utf-8'))
            self.cpf_token = base64.urlsafe_b64encode(cpf_encrypted).decode('utf-8')
        super().save(*args, **kwargs)

    def get_decrypted_cpf(self):
        """Função para descriptografar o CPF quando necessário."""
        cpf_encrypted = base64.urlsafe_b64decode(self.cpf_token.encode('utf-8'))
        return cipher_suite.decrypt(cpf_encrypted).decode('utf-8')

    def __str__(self):
        return self.nome
