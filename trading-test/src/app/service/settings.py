from pathlib import Path
import os

BASE_DIR: Path = Path(__file__).resolve().parent.parent

SECRET_KEY: str = 'django-insecure-xsj=*abte(0nz&ds2m#u4pn&q53i@$0=5rvh7w_m!$ho+sc4hh'

DEBUG: bool = True

ALLOWED_HOSTS = ['*']

INSTALLED_APPS: list = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'rest_framework',
  'corsheaders'
]

MIDDLEWARE: list = [
  'corsheaders.middleware.CorsMiddleware',
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ALLOW_ALL_ORIGINS: bool = True

ROOT_URLCONF: str= 'app.service.urls'

TEMPLATES: list = [
  {
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION: str = 'app.service.wsgi.application'

# DATABASES: dict = {
#   'default': {
#     'ENGINE': 'django.db.backends.sqlite3',
#     'NAME': BASE_DIR / 'db.sqlite3',
#   }
# }

AUTH_PASSWORD_VALIDATORS: list = [
  { 'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator' },
  { 'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator' },
  { 'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator' },
  { 'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator' ''},
]

LANGUAGE_CODE: str = 'en-us'

TIME_ZONE: str = 'UTC'

USE_I18N: bool = True

USE_L10N: bool = True

USE_TZ: bool = True



STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]
# STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEFAULT_AUTO_FIELD: str = 'django.db.models.BigAutoField'

APPEND_SLASH: bool = False
