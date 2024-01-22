from django.core.management.base import BaseCommand
from hw1_app.models import Items


class Command(BaseCommand):
    help = 'Create a new client'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price')
        parser.add_argument('quantity', type=int)

    def handle(self, *args, **kwargs):
        item = Items(
            title=kwargs.get('title'),
            description=kwargs.get('description'),
            price=kwargs.get('price'),
            quantity=kwargs.get('quantity')
        )
        item.save()
        self.stdout.write('Item created')
