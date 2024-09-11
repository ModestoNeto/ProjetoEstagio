from django.urls import path
from .views import cadastrar_aluno, lista_alunos, login_view, home, agendamento_view, diario_turma_view, faltas_view,logout_view

urlpatterns = [
    path('cadastrar/', cadastrar_aluno, name='cadastrar_aluno'),
    path('alunos/', lista_alunos, name='lista_alunos'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),
    path('agendamento/', agendamento_view, name='agendamento'),
    path('diario-turma/', diario_turma_view, name='diario_turma'),
    path('faltas/', faltas_view, name='faltas'),
    path('logout/', logout_view, name='logout'),
]




