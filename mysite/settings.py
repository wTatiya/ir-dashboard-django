SECRET_KEY = '9f4ac7a0d54142a03913b1d95bea142b'
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = ['django.contrib.staticfiles']
ROOT_URLCONF = 'mysite.urls'
MIDDLEWARE = []

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['myapp/templates'],
    'APP_DIRS': True,
    'OPTIONS': {},
}]

WSGI_APPLICATION = 'mysite.wsgi.application'
STATIC_URL = '/static/'
