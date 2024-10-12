from django.contrib import admin
from django.urls import path, include  # Importar 'include' para incluir as URLs de 'app_escola'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app_escola.urls')),  # Incluir as URLs definidas no 'app_escola/urls.py'
]
