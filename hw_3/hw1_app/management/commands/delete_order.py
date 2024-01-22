from django.core.management.base import BaseCommand
from hw_3.hw1_app.models import Items, Client, Order

class Command(BaseCommand):
    help = "Delete order by id"

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def handle(self, *args, **kwargs):
        pk = kwargs.get('pk')
        order = Order.objects.filter(pk=pk).first()

        self.stdout.write(f'{order}')
        order.delete()

