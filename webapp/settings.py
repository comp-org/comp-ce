"""
Django settings for webapp project.

Generated by 'django-admin startproject' using Django 2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY', 'test-key-only')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False if os.environ.get('DEBUG', 'False') == 'False' else True

ALLOWED_HOSTS = ['*']
# enforce HTTPS/SSL
SECURE_SSL_REDIRECT = True
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'webapp.apps.core',
    'webapp.apps.pages',
    'webapp.apps.upload',
    'webapp.apps.users',

    # 'allauth', # new
    # 'allauth.account', # new
    # 'allauth.socialaccount', # new
    # 'allauth.socialaccount.providers.github', # new
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR + '/templates/'],
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

WSGI_APPLICATION = 'webapp.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

TEST_DATABASE = {
    'TEST': {
        'ENGINE': 'django.db.backends.postgresql',
        'USER': os.environ.get('DATABASE_USER', 'postgres'),
        'NAME': 'test_db',
        'PASSWORD': os.environ.get('DATABASE_PW', ''),
    }
}
if os.environ.get('DATABASE_URL', None):  # DATABASE_URL var is set
    DATABASES = {'default': dj_database_url.config()}
    DATABASES.update(TEST_DATABASE)
else:  # DATABASE_URL is not set--try default
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'taxcalc',
            'USER': os.environ.get('DATABASE_USER', 'postgres'),
            'PASSWORD': os.environ.get('DATABASE_PW', ''),
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }
    DATABASES.update(TEST_DATABASE)


# Authentication backends--use django and django-allauth
# AUTHENTICATION_BACKENDS = (
#     "django.contrib.auth.backends.ModelBackend",
#     # "allauth.account.auth_backends.AuthenticationBackend",
# )
#
SITE_ID = 1

# Login routing
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# For custom user class
AUTH_USER_MODEL = 'users.User'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Email backend for developing pw reset functionality
EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = os.path.join(BASE_DIR, "sent_emails")

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]


EMAIL_BACKEND = "sgbackend.SendGridBackend"
SENDGRID_API_KEY=os.environ.get("SENDGRID_API_KEY", "dne")