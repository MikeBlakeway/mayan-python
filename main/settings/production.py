from .settings import *
import dj_database_url


DEBUG = False


ALLOWED_HOSTS = [
    config('ALLOWED_HOSTS'),
    'mayanwebstudio.co.uk',
]


# INSTALLED_APPS += (
#     'whitenoise.runserver_nostatic',
# )


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
# load database from the DATABASE_URL environment variable
DATABASES = {}
DATABASES['default'] = dj_database_url.config(conn_max_age=600)


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


STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage
