# taxi_service/settings.py

# ... (resto do arquivo)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'taxi',  # <-- ADICIONAR AQUI
]

# ... (resto do arquivo)

# Definir o modelo de usuário customizado
AUTH_USER_MODEL = 'taxi.Driver' # <-- ADICIONAR AQUI

# Dentro de settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',  # <-- Necessário
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware', # <-- Necessário
    'django.contrib.messages.middleware.MessageMiddleware',    # <-- Necessário
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Dentro de settings.py

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates', # <-- Necessário
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


# No final de settings.py

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
