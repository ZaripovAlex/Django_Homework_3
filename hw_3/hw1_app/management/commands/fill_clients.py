import datetime
from django.core.management.base import BaseCommand
from hw1_app.models import Client


class Command(BaseCommand):
    help = 'Fill clients'
    def add_arguments(self, parser):
        parser.add_argument('count', type=int)
    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(count):
            client = Client(
                name=f'Client{i}',
                email=f'client{i}@example.com',
                phone_number=f'+7904{i}8{i}4{i}7{i}',
                address=f'address{i}',
                date=datetime.date(2000, 1, 1)
            )
            self.stdout.write(f'{count} client created')
            client.save()
