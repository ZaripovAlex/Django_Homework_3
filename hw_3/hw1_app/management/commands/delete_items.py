from django.core.management.base import BaseCommand
from hw1_app.models import Items


class Command(BaseCommand):
    help = "Delete item by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        item = Items.objects.filter(pk=pk).first()

        self.stdout.write(f'{item}')
        item.delete()