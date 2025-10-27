SECRET_KEY = 'replace-this-with-a-secure-key'
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
