import os
from pathlib import Path
from dotenv import load_dotenv


# ./lyceum/lyceum/.env
if os.path.exists(dotenv_path := os.path.join(os.path.dirname(__file__), '.env')):
    load_dotenv(dotenv_path)

DEBUG = os.environ['DEBUG']

SECRET_KEY = os.environ['SECRET_KEY']

BASE_DIR = Path(__file__).resolve().parent.parent

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]

INTERNAL_IPS = [
    '127.0.0.1',
    'localhost',
]

INSTALLED_APPS = (
    'homepage.apps.HomepageConfig',
    'catalog.apps.CatalogConfig',
    'about.apps.AboutConfig',
    'users.apps.UsersConfig',
    'rating.apps.RatingConfig',
    
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'debug_toolbar',
)

MIDDLEWARE = (
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'lyceum.urls'

TEMPLATES = (
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': (
            BASE_DIR / 'templates',
        ),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': (
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ),
        },
    },
)

WSGI_APPLICATION = 'lyceum.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = (
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
)

LANGUAGE_CODE, TIME_ZONE = 'ru', 'UTC'

USE_I18N, USE_L10N, USE_TZ = True, True, True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# STATIC SETTINGS
STATIC_URL = 'static/'

STATICFILES_DIRS = (
    BASE_DIR / "static",
    '/var/www/static/',
)

# LOGIN & REGISTER
LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = '/auth/profile'

EMAIL_HOST = 'smtp.yandex.ru'
EMAIL_HOST_USER = 'noreply.lyceum@yandex.ru'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_PWD')
