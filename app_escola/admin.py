from django.contrib import admin
from .models import Aluno

# Customizar a exibição no admin
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'get_decrypted_cpf', 'telefone', 'endereco', 'genero')  # Exibe campos no admin
    search_fields = ('nome', 'cpf_token')  # Campos que podem ser buscados

    # Método para exibir o CPF descriptografado no admin
    def get_decrypted_cpf(self, obj):
        return obj.get_decrypted_cpf()

    # Modificar o nome da coluna no admin
    get_decrypted_cpf.short_description = 'CPF (Descriptografado)'

# Registrar o modelo Aluno no admin
admin.site.register(Aluno, AlunoAdmin)
