# main/services.py

from .models import Aluno
from django.db import IntegrityError


def criar_aluno(nome, telefone, email, data_nascimento, description, cpf, user):
    """
    Função para criar um novo aluno no banco de dados.
    :param nome: Nome do aluno
    :param telefone: Telefone do aluno
    :param email: Email do aluno
    :param data_nascimento: Data de nascimento do aluno
    :param description: Descrição do aluno
    :param cpf: CPF do aluno
    :param user: Usuário associado ao aluno
    :return: Objeto Aluno ou erro (string)
    """
    try:
        aluno = Aluno.objects.create(
            nome=nome,
            telefone=telefone,
            email=email,
            data_nascimento=data_nascimento,
            description=description,
            cpf=cpf,
            user=user
        )
        return aluno  # Retorna o objeto Aluno criado
    except IntegrityError as e:
        return f"Erro ao criar aluno: {str(e)}"  # Retorna o erro caso ocorra
