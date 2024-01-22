import datetime
import random

from django.core.management.base import BaseCommand
from hw1_app.models import Items

class Command(BaseCommand):
    help = 'Fill clients'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(count):
            items = Items(
                title=f'Items{i}',
                description=f'Lorem ipsum dolor sit amet, consectetur adip',
                price=random.randint(100, 999),
                quantity=random.randint(1, 100),
                date=datetime.date(2000, 1, 1)
            )
            self.stdout.write(f'{count} items created')
            items.save()
