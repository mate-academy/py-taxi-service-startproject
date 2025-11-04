# taxi_service/settings.py

INSTALLED_APPS = [
    # стандартні додатки Django...
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # наш додаток
    'taxi',
]

# Вкажемо кастомну модель користувача
AUTH_USER_MODEL = 'taxi.Driver'
