from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
import os

class Command(BaseCommand):
    help = 'Create a superuser if not exists'

    def handle(self, *args, **kwargs):
        User = get_user_model()
        superuser_username = os.getenv('DJANGO_SUPERUSER_USERNAME')
        superuser_email = os.getenv('DJANGO_SUPERUSER_EMAIL')
        superuser_password = os.getenv('DJANGO_SUPERUSER_PASSWORD')

        if superuser_username and superuser_email and superuser_password:
            if not User.objects.filter(username=superuser_username).exists():
                User.objects.create_superuser(
                    username=superuser_username,
                    email=superuser_email,
                    password=superuser_password
                )
                self.stdout.write(self.style.SUCCESS('Successfully created superuser'))
            else:
                self.stdout.write(self.style.SUCCESS('Superuser already exists'))
        else:
            self.stdout.write(self.style.ERROR('Superuser credentials are not set in environment variables'))
