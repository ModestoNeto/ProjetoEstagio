from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # Página inicial
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar_aluno'),  # Página de cadastro de alunos
    path('alunos/', views.lista_alunos, name='lista_alunos'),           # Página para listar alunos
    path('login/', views.login_view, name='login'),                    # Página de login
    path('logout/', views.logout_view, name='logout'),                 # Página de logout
    path('agendamento/', views.agendamento_view, name='agendamento'),  # Página de agendamento
    path('diario/', views.diario_turma_view, name='diario_turma'),     # Página de diário de turma
    path('faltas/', views.faltas_view, name='faltas'),                 # Página de controle de faltas
]
