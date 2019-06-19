"""
Django settings for hijri_calendar_site project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

from envs import env

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '!r71&*14evg0slrxi+lqkrl5uq%&-oz5=y@=6^7ck&wglssv_@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', False, var_type='boolean')

ALLOWED_HOSTS = [
    '0.0.0.0',
    '127.0.0.1',
    'localhost',
    'mooncal.azurewebsites.net',
    'mooncalendar.azurewebsites.net'
    ]

CSRF_TRUSTED_ORIGINS = ALLOWED_HOSTS


# Application definition

INSTALLED_APPS = [
    'hijri_calendar_app.apps.HijriCalendarWebsiteConfig',
    'hijri_calendar_api.apps.HijriCalendarApiConfig',
    'material',
    'material.theme.amber',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'rest_framework',
    'django_admin_shell',
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

ROOT_URLCONF = 'hijri_calendar_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
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

WSGI_APPLICATION = 'hijri_calendar_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

sql_lite_db_path = os.path.join(BASE_DIR, 'db.sqlite3')
if DEBUG and not env('DATABASE_ENGINE'):
    print("sql lite db is located at:", sql_lite_db_path)

DATABASES = {
    'default': {
        'ENGINE': env('DATABASE_ENGINE', 'django.db.backends.sqlite3'),
        'NAME': env('DATABASE_NAME', sql_lite_db_path),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT')
    }
}
# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'UserAttributeSimilarityValidator'
            ),
            },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'MinimumLengthValidator'
            ),
            },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'CommonPasswordValidator'
            ),
            },
    {
        'NAME': (
            'django.contrib.auth.password_validation.'
            'NumericPasswordValidator'
            ),
            },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
STATIC_URL = env('STATIC_URL', '/static/')

STATICFILES_DIR = (
    os.path.join(BASE_DIR, 'static'),
)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


NOTEBOOK_ARGUMENTS = [
    # '--notebook-dir', 'notebooks',
    # exposes IP and port
    '--ip=0.0.0.0',
    '--port=8888',
    '--allow-root',
    # disables the browser
    '--no-browser',
 ]


def print_settings():
    if DEBUG:
        from django.conf import settings
        message = (
            f"You are using [{settings.DATABASES['default']['ENGINE']}] "
            f"as your database engine\n"
            f"You are using [{settings.DATABASES['default']['NAME']}] "
            f"as your default database\n"
            )
        print(message)


# print_settings()

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticatedOrReadOnly',
        ],
    'DEFAULT_PAGINATION_CLASS': (
        'rest_framework.pagination.'
        'PageNumberPagination'
        ),
    'PAGE_SIZE': 20
}

# django-admin-shell settings
ADMIN_SHELL_ENABLE = True
ADMIN_SHELL_ONLY_FOR_SUPERUSER = True
ADMIN_SHELL_ONLY_DEBUG_MODE = True
