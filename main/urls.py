from django.contrib.auth import views as auth_views
from django.urls import path
from .views import alunoView, alunoIDview, criarAlunoView, atualizarAlunoView 
urlpatterns = [
    path('aluno_view/', alunoView, name='aluno_view'),
    path('aluno/<int:id>/', alunoIDview, name='aluno_id_view'),
    path('criar_aluno/', criarAlunoView, name='criar_aluno'),
    path('aluno/<int:id>/update/', atualizarAlunoView, name='atualizar_aluno'),
    path('', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
