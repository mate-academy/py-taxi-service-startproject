from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
# PARA DESENVOLVIMENTO/TESTES, VOCÊ PODE DEIXAR ISSO ASSIM, MAS TROQUE PARA PRODUÇÃO!
SECRET_KEY = 'django-insecure-sua-chave-secreta-aqui-mude-isso'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [] # Para testes locais, pode deixar vazio ou adicionar '127.0.0.1'


# --- CONFIGURAÇÕES DE APLICAÇÕES E MIDDLEWARE (Corrigido) ---

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taxi',  # Sua aplicação
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # <-- CORRIGIDO
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # <-- CORRIGIDO
    'django.contrib.messages.middleware.MessageMiddleware',    # <-- CORRIGIDO
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'taxi_service.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # <-- CORRIGIDO
        'DIRS': [],
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

# --- CONFIGURAÇÃO DE BANCO DE DADOS (Corrigido) ---

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3', # <-- CORRIGIDO
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# --- CONFIGURAÇÕES DE AUTENTICAÇÃO ---

# Definir o modelo de usuário customizado
AUTH_USER_MODEL = 'taxi.Driver' # <-- CORRIGIDO

# --- CONFIGURAÇÕES DE LINGUAGEM E ZONA HORÁRIA ---

LANGUAGE_CODE = 'pt-br' # Sugestão, se estiver no Brasil

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# --- CONFIGURAÇÕES DE ARQUIVOS ESTÁTICOS ---

STATIC_URL = 'static/'

# --- CORREÇÃO PARA AVISOS (W042) ---
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField' # <-- CORRIGIDO
