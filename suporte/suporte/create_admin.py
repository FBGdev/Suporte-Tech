import django
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "suporte.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username="admin").exists():
    User.objects.create_superuser("admin", "fabianodev@yahoo.com", "admin@senha")
