from django.db import models
import hashlib

def hash_cpf(cpf):
    """Função para hash do CPF antes de salvar."""
    return hashlib.sha256(cpf.encode('utf-8')).hexdigest()

class Student(models.Model):
    """Modelo para representar um aluno."""
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=11, unique=True)  # CPF deve ter 11 dígitos
    address = models.CharField(max_length=255)
    cpf_hash = models.CharField(max_length=64, editable=False)  # CPF armazenado como hash

    def save(self, *args, **kwargs):
        """Sobrescreve o método save para salvar o hash do CPF."""
        if not self.cpf_hash:
            self.cpf_hash = hash_cpf(self.cpf)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
