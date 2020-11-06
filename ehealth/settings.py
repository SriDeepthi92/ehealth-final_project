"""
Django settings for django_school project.

Generated by 'django-admin startproject' using Django 2.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""

import os

from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd$pxg6fisc4iwzk&vz^s_d0lkf&k63l5a8f!obktw!jg#4zvp3'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_tables2',
    'crispy_forms',
    #'django_extensions',

    'clinic',
    'social_django',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'social_django.middleware.SocialAuthExceptionMiddleware',

]

ROOT_URLCONF = 'django_school.urls'

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
                'social_django.context_processors.backends',
                'social_django.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'django_school.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default':  {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'pddatabase',
        'USER': 'postgres',
        'PASSWORD': '*****',
        'HOST': 'localhost',
        'PORT': '5432',

    }
}


AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',
    'social.backends.twitter.TwitterOAuth',
    #'social_auth.backends.google.GoogleOAuthBackend',
    #'social_auth.backends.google.GoogleBackend',
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.google.GoogleOAuth2',
    'django.contrib.auth.backends.ModelBackend',
    'social_core.backends.google.GoogleOAuth2',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    #'oauth2_login_client.backends.OAuthBackend',
    #'github_oauth.authentication.GithubOAuthentication',
)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]


# Custom Django auth settings

AUTH_USER_MODEL = 'clinic.User'

LOGIN_URL = 'login'

LOGOUT_URL = 'logout'

LOGIN_REDIRECT_URL = 'home'

LOGOUT_REDIRECT_URL = 'home'

# Messages built-in framework

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-secondary',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}


# Third party apps configuration

CRISPY_TEMPLATE_PACK = 'bootstrap4'
GOOGLE_MAPS_API_KEY = 'AIzaSyCmgpeiilp1NmGb2_zCQ_CpRQi19RM4WRc'
SOCIAL_AUTH_GITHUB_KEY = '70f4830d004a11f86ecb'
SOCIAL_AUTH_GITHUB_SECRET = '76f958cb61a2d5c7789f58775dbed149dd308768'
"""
GITHUB_CLIENT_ID = '70f4830d004a11f86ecb'
GITHUB_CLIENT_SECRET = '76f958cb61a2d5c7789f58775dbed149dd308768'
GITHUB_REDIRECT_URI = 'http://localhost:8000/accounts/login.html'
"""
SOCIAL_AUTH_URL_NAMESPACE = 'social'

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '1024381235457-0g5qgnsj602s1q07o4o771out38lkccn.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'hnMInIuKqjUl6x4UapzFNGEl'


SOCIAL_AUTH_TWITTER_KEY = 'sqVEId4RrXkUc0DBBCpzDIkav'
SOCIAL_AUTH_TWITTER_SECRET = 'LcWGmnnAq2nFmfsCPOiXTz8cfstbjeDQx1UPgidZIgNCPyMYKQ'

SOCIAL_AUTH_FACEBOOK_KEY = '386135722770069'
SOCIAL_AUTH_FACEBOOK_SECRET = '17362eb004f5838b98a239eeeae37101 '
