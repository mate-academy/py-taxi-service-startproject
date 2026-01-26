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

# ... (resto do arquivo)
