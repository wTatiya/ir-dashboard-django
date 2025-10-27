SECRET_KEY = os.environ.get('SECRET_KEY', '9f4ac7a0d54142a03913b1d95bea142b')
DEBUG = True
ALLOWED_HOSTS = ['*']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

ROOT_URLCONF = 'mysite.urls'
MIDDLEWARE = ['django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',]

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': ['myapp/templates'],
    'APP_DIRS': True,
    'OPTIONS': {},
}]

WSGI_APPLICATION = 'mysite.wsgi.application'
STATIC_URL = '/static/'
