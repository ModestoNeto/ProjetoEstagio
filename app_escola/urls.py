from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='app_escola/login.html'), name='login'),  # Definir a tela de login como inicial
    path('home/', views.home, name='home'),  # Página inicial após login
    path('logout/', auth_views.LogoutView.as_view(template_name='app_escola/logout.html'), name='logout'),  # URL de logout usando template `logout.html`
    path('cadastrar_aluno/', views.cadastrar_aluno, name='cadastrar_aluno'),
    path('lista_alunos/', views.lista_alunos, name='lista_alunos'),
    path('agendamento/', views.agendamento, name='agendamento'),
    path('diario_turma/', views.diario_turma, name='diario_turma'),
    path('faltas/', views.faltas, name='faltas'),
]
