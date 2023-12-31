from pathlib import Path
import os
import environ
import dj_database_url 

env = environ.Env()
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG', default=False)

ALLOWED_HOSTS = [env('ALLOWED_HOSTS')]

AUTH_USER_MODEL = 'profile_user.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Django tailwind
    'tailwind',
    'theme',
    'compressor',
    #crispy_forms
    #"crispy_tailwind",

    # Django_phonenumber_field
    "phonenumber_field",

    # Apps_local
    'profile_user',
    'client',
    'inventory',
    'service',
    'administrator',
    'booking',

    # import_export
    'import_export',
]

# Django tailwind
TAILWIND_APP_NAME = 'theme'
INTERNAL_IPS = [
    "127.0.0.1",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"

CRISPY_TEMPLATE_PACK = "tailwind"

#Linux/Mac
NPM_BIN_PATH = '/usr/local/bin/npm'

#Windows
#NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"

MIDDLEWARE = [

    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'project_admin.middleware.ProfileLoginMiddleware',   

]

ROOT_URLCONF = 'project_admin.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

WSGI_APPLICATION = 'project_admin.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases


DATABASES = {
    'default': dj_database_url.config(
        default=env('DATABASE_URL')
    )
}
"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
"""

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

TIME_ZONE = 'America/Bogota'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media
MEDIA_URL ='/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

COMPRESS_ROOT = BASE_DIR / 'static'

COMPRESS_ENABLED = env('COMPRESS_ENABLED')

STATICFILES_FINDERS = ("django.contrib.staticfiles.finders.AppDirectoriesFinder", 'compressor.finders.CompressorFinder',)

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_REDIRECT_URL = '/booking/gestion/'

LOGIN_URL = '/'

LOGOUT_REDIRECT_URL = LOGIN_URL

#STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

