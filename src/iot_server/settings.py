"""
Django settings for iot_server project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-i&uv2ho(x=lzk#3qwc4^!-ut$67h=h5o(#)&pgnqsrbd3$uj3t'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third party apps
    'django_clickhouse',
    'django_celery_beat',
    'rest_framework',
    'rest_framework.authtoken',
    'dj_rest_auth',
    # Yet another Swagger generator
    'drf_yasg',
    'corsheaders',

    # Local apps
    'device',
    'dashboard',
    'event',
    'notification',
    'api',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'iot_server.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            # 'templates'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.media',
                # 'django.template.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'iot_server.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'djongo',
        'NAME': os.environ.get("MONGODB_NAME"),
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': f'mongodb://{os.environ.get("MONGODB_USERNAME")}:{os.environ.get("MONGODB_PASSWORD")}@{os.environ.get("MONGODB_HOST")}:{os.environ.get("MONGODB_PORT")}'
        }  
    }
}

# django-clickhouse library setup
CLICKHOUSE_DATABASES = {
    'default': {
        'db_url': f'http://{os.environ.get("CLICKHOUSE_DATABASE_HOST")}:{os.environ.get("CLICKHOUSE_DATABASE_PORT")}',
        'db_name': os.environ.get("CLICKHOUSE_DATABASE_NAME"),
        'username': os.environ.get("CLICKHOUSE_DATABASE_USERNAME"),
        'password': os.environ.get("CLICKHOUSE_DATABASE_PASSWORD"),
        'migrate': True
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = '/home/application/static'

MEDIA_ROOT = '/home/application/media'
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL = 'device.User'
TIME_FORMAT_STRING = "%Y-%m-%dT%H:%M:%SZ"
DEVICE_PROPERTY_UPDATE_DELAY_MINUTES = 10
WEATHER_DATA_CACHE_MINUTES = 30
DEFAULT_SYNC_FREQUENCY_MINUTES = 10

# API keys
OPENWEATHERMAP_API_KEY = os.environ.get("OPENWEATHERMAP_API_KEY")

# Permissions config
PERMISSIONS_SUPER_USER = "PERMISSIONS_SUPER_USER"
PERMISSIONS_ADMIN = "PERMISSIONS_ADMIN"
PERMISSIONS_DEV_USER = "PERMISSIONS_DEV_USER"

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'device.authentication.DeviceAuthentication',
    ),
}

CORS_ALLOWED_ORIGINS = [
    "http://*",
    "https://*",
]

CORS_ALLOW_ALL_ORIGINS = True
