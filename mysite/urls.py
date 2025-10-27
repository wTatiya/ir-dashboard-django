from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from django.http import HttpResponse
from django.core.management import call_command
from django.contrib.auth import get_user_model


def index(request):
    return render(request, 'index.html')


# ✅ Add this route to manually trigger migrations
def run_migrations(request):
    call_command('migrate')
    return HttpResponse("Migrations complete.")


# ✅ Add this route to create an admin account
def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'changeme123')
        return HttpResponse("Superuser created.")
    return HttpResponse("Superuser already exists.")


urlpatterns = [
    path('', index),
    path('admin/', admin.site.urls),
    path('run-migrations/', run_migrations),           # << you likely missed this line!
    path('create-superuser/', create_superuser),       # << and maybe this one too
]
