from django.core.management.base import BaseCommand
from hw1_app.models import Client

class Command(BaseCommand):
    help = 'Create a new client'
    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone', type=str)
        parser.add_argument('address', type=str)
    def handle(self, *args, **kwargs):
        client = Client(
            name= kwargs.get('name'),
            email= kwargs.get('email'),
            phone_number=kwargs.get('phone'),
            address=kwargs.get('address')
        )
        client.save()
        self.stdout.write('Client created')
