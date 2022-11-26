"""
Django settings for iot_server project.

Generated by 'django-admin startproject' using Django 4.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "___CHANGE____ME___")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.getenv("DJANGO_DEBUG", False) == 'True'

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", '').split(',')
CSRF_TRUSTED_ORIGINS = os.getenv("DJANGO_CSRF_TRUSTED_ORIGINS", '').split(',')

# Application definition

INSTALLED_APPS = [
    'daphne',
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
ASGI_APPLICATION = "iot_server.asgi.application"

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
        'NAME': os.getenv("MONGODB_NAME"),
        'ENFORCE_SCHEMA': False,
        'CLIENT': {
            'host': f'mongodb://{os.getenv("MONGODB_USERNAME")}:{os.getenv("MONGODB_PASSWORD")}@{os.getenv("MONGODB_HOST")}:{os.getenv("MONGODB_PORT")}'
        }  
    }
}

# django-clickhouse library setup
CLICKHOUSE_DATABASES = {
    'default': {
        'db_url': f'http://{os.getenv("CLICKHOUSE_DATABASE_HOST")}:{os.getenv("CLICKHOUSE_DATABASE_PORT")}',
        'db_name': os.getenv("CLICKHOUSE_DATABASE_NAME"),
        'username': os.getenv("CLICKHOUSE_DATABASE_USERNAME"),
        'password': os.getenv("CLICKHOUSE_DATABASE_PASSWORD"),
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
DEVICE_PROPERTY_UPDATE_DELAY_MINUTES = os.getenv("DEVICE_PROPERTY_UPDATE_DELAY_MINUTES", 10)
WEATHER_DATA_CACHE_MINUTES = os.getenv("WEATHER_DATA_CACHE_MINUTES", 30)
DEFAULT_SYNC_FREQUENCY_MINUTES = os.getenv("DEFAULT_SYNC_FREQUENCY_MINUTES", 10)

# API keys
OPENWEATHERMAP_API_KEY = os.getenv("OPENWEATHERMAP_API_KEY")

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

REDIS_HOST = os.getenv("REDIS_HOST")

if REDIS_HOST:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels_redis.core.RedisChannelLayer",
            "CONFIG": {
                "hosts": [(REDIS_HOST, 6379)],
            },
        },
    }

    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": f'redis://{REDIS_HOST}',
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
            }
        }
    }
else:
    CHANNEL_LAYERS = {
        "default": {
            "BACKEND": "channels.layers.InMemoryChannelLayer"
        }
    }
