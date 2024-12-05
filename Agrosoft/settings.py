"""
Django settings for Agrosoft project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
from datetime import timedelta

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y25f0nlxx-^y1tc$12**4)gsf=uy7wkcvt%ahr(*l)cf=7#m5i'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']
    


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps.Usuarios.roles',
    'apps.Usuarios.permisos',
    'apps.Usuarios.rol_permiso',
    'apps.Usuarios.usuarios',
    'apps.Usuarios.usuario_rol',
    'apps.Usuarios.roles_acciones',
    'apps.Cultivo.bancal',
    'apps.Cultivo.tipo_plaga',
    'apps.Cultivo.plagas',
    'apps.Cultivo.especies',
    'apps.Cultivo.tipo_especies',
    'apps.Cultivo.cultivos',
    'apps.Cultivo.fase_lunar',
    'apps.Cultivo.tipo_control',
    'apps.Cultivo.semillero',
    'apps.Cultivo.afecciones',
    'apps.Cultivo.controles',
    'apps.Cultivo.productos_control',
    'apps.Cultivo.plantaciones',
    'apps.Cultivo.tipo_actividad',
    'apps.Cultivo.actividades',
    'apps.Cultivo.tareas',
    'apps.Iot.datos_meteorologicos',
    'apps.Iot.sensores',
    'apps.Iot.configuraciones',
    'apps.Iot.evotranspiraciones',
    'apps.Finanzas.pagos',
    'apps.Inventario.bodega',
    'apps.Inventario.bodega_insumo',
    'apps.Inventario.bodega_herramienta',
    'apps.Inventario.herramientas',
    'apps.Inventario.insumos',
     'rest_framework',
    'rest_framework_simplejwt',
    'drf_yasg',
    'apps.Cultivo.residuos',
    'apps.Cultivo.tipos_residuos',
    'apps.Cultivo.programacion',
    'apps.Cultivo.cosechas',
    'apps.Cultivo.lotes',
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

ROOT_URLCONF = 'Agrosoft.urls'

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

WSGI_APPLICATION = 'Agrosoft.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Agrosoft',
        'USER': 'postgres',
        'PASSWORD': 'root',
        'HOST': 'localhost', 
        'PORT': '5432',
        'OPTIONS': {
            'client_encoding': 'UTF8',
        },
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = './static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=60),  
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7), 
    'ROTATE_REFRESH_TOKENS': True,  
    'BLACKLIST_AFTER_ROTATION': True,  

    'ALGORITHM': 'HS256',  
    'SIGNING_KEY': SECRET_KEY, 
    'AUTH_HEADER_TYPES': ('Bearer',),  
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
}

AUTH_USER_MODEL = 'usuarios.Usuarios'
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
