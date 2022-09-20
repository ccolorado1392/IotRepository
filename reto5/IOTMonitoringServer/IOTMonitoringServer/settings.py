"""
Django settings for IOTMonitoringServer project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

import os
from pathlib import Path
from django.contrib import messages

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-bu+)8ft@9+qd*#e#f_s@wkyv2tmq+#!a^3j15h3kjk^jzksu0j'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost", "35.174.242.92"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'control',
    'receiver',
    'viewer'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IOTMonitoringServer.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "viewer", "templates")],
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

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

WSGI_APPLICATION = 'IOTMonitoringServer.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "iot_data",  # Nombre de la base de datos
        "USER": "dbadmin",  # Nombre de usuario
        "PASSWORD": "uniandesIOT1234*",  # Contraseña
        "HOST": "44.195.66.0",  # Dirección IP de la base de datos
        "PORT": "",  # Puerto de la base de datos
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-co'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

STATIC_URL = 'static/'

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "static", "media")

STATICFILES_DIRS = (os.path.join(PROJECT_ROOT, "static/"),)

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = '/login/'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Dirección del bróker MQTT
MQTT_HOST = "3.234.205.158"

# Puerto del bróker MQTT
MQTT_PORT = 8082

# Credenciales para el usuario suscriptor del bróker MQTT
MQTT_USER = "admin"
MQTT_PASSWORD = "admin"

# Credenciales para el usuario publicador del bróker MQTT
MQTT_USER_PUB = "admin2"
MQTT_PASSWORD_PUB = "admin2"

# Tópico a suscribir. "+/+/+/+/out" se suscribe únicamente a los
# tópicos con forma <país>/<estado>/<ciudad>/<usuario>/out.
TOPIC = "+/+/+/+/out"

# Opción para habilitar la transmisión de mensajes segura
MQTT_USE_TLS = False

# Ubicación del archivo de certificado para conexión TLS con el bróker MQTT
CA_CRT_FILE = "ssl/ca.crt"
CA_CRT_PATH = os.path.join(os.path.dirname(__file__), CA_CRT_FILE)
