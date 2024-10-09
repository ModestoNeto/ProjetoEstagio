from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='app_escola/login.html'), name='login'),
    path('home/', views.home, name='home'),
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('lista_alunos/', views.lista_alunos, name='lista_alunos'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('diario_turma/', views.diario_turma, name='diario_turma'),  # URL para a página de diário de turma
    path('perfil/', views.perfil, name='perfil'),
]
