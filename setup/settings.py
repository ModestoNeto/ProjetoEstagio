from pathlib import Path
import os
from dotenv import load_dotenv  # Importar `load_dotenv` para carregar variáveis do .env
from cryptography.fernet import Fernet  # Importar Fernet para gerenciar a criptografia

# Carregar as variáveis do arquivo .env
load_dotenv()

# Caminho base do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Carregar a chave de criptografia e secret key a partir do .env
SECRET_KEY = os.getenv('SECRET_KEY')  # Carregar a SECRET_KEY do .env

# Verificar se a chave foi carregada corretamente
if not SECRET_KEY:
    raise ValueError("A chave SECRET_KEY não foi encontrada no arquivo .env")

# Usar a mesma SECRET_KEY para instanciar o Fernet (cripto)
cipher_suite = Fernet(SECRET_KEY.encode())  # Cria a instância Fernet usando a mesma chave como bytes

# Carregar outras variáveis de ambiente
DEBUG = os.getenv('DEBUG', 'False') == 'True'  # Converte 'True'/'False' para valor booleano
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1').split(',')  # Transforma a lista de hosts permitidos em lista Python

# Aplicativos instalados
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app_escola',  # Aplicativo 'app_escola'
]

# Middlewares do Django
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuração da URL principal
ROOT_URLCONF = 'setup.urls'

# Configuração dos templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Diretório de templates (opcional)
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Configuração de WSGI para o projeto
WSGI_APPLICATION = 'setup.wsgi.application'

# Configuração do banco de dados
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validação de senha
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Configurações de localização e idioma
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Fortaleza'
USE_I18N = True
USE_TZ = True

# Configuração dos arquivos estáticos
STATIC_URL = '/static/'  # URL usada para servir os arquivos estáticos no navegador

# Diretórios para buscar arquivos estáticos (CSS, JS, imagens)
STATICFILES_DIRS = [
    BASE_DIR / 'app_escola' / 'static',  # Diretório onde estão os arquivos estáticos do app 'app_escola'
]

# Diretório onde os arquivos estáticos serão armazenados após executar `collectstatic`
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Configuração do diretório de mídia (opcional)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Tipo de campo padrão para chaves primárias automáticas
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
