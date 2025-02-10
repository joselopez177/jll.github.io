import dj_database_url
import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.environ.get("DEBUG", "False").lower() == "true"
DEBUG = True
#ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS").split(" ")
#ALLOWED_HOSTS = ["localhost", "192.168.0.121", "127.0.0.1"]
ALLOWED_HOSTS = ['https://jll-github-io.onrender.com', 'www.https://jll-github-io.onrender.com', '127.0.0.1', '[::1]']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    'store',
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
     'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ecommerce.urls'

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

WSGI_APPLICATION = 'ecommerce.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases



# Asegúrate de que esta línea esté correcta
import dj_database_url

# Asegúrate de que esta línea esté correcta
#SEGUN COPILOT:
#database_url = os.getenv("DATABASE_URL", "postgres://jllbaseposgre_ld7e_user:J8VAzjzsZYRdYeBR7b0mvIvYZwUjZcgI@dpg-cuhtqel2ng1s73dulvhg-a.oregon-postgres.render.com:5432/jllbaseposgre_ld7e")
#("DATABASE_URL", "postgres://USER:PASSWORD@HOST:PORT/NAME")

DATABASES = {
    "default": dj_database_url.parse("postgresql://jllbaseposgre_ld7e_user:J8VAzjzsZYRdYeBR7b0mvIvYZwUjZcgI@dpg-cuhtqel2ng1s73dulvhg-a.oregon-postgres.render.com/jllbaseposgre_ld7e")
}



#)

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-mx'

TIME_ZONE = 'America/México/Hermosillo'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

MEDIA_URL = '/images/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/images')
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'