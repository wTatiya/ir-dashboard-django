from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth import get_user_model


# ✅ Renders index.html for the homepage
def index(request):
    return render(request, 'index.html')


# ✅ Runs migrations manually (visit /run-migrations/)
def run_migrations(request):
    call_command('migrate')
    return HttpResponse("Migrations complete.")


# ✅ Creates a superuser (visit /create-superuser/ once)
def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'changeme123')
        return HttpResponse("Superuser created.")
    return HttpResponse("Superuser already exists.")


# ✅ All available routes
urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('run-migrations/', run_migrations),
    path('create-superuser/', create_superuser),
]
