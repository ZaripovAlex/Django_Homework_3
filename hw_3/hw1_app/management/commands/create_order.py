from django.core.management.base import BaseCommand
from hw1_app.models import Items, Client, Order

class Command(BaseCommand):
    help = 'Create order'

    def handle(self, *args, **kwargs):
        client_id = 1
        item_id_list = [1, 2, 3, 4, 5]
        print(item_id_list)
        sum = 0
        items = []
        for item_id in item_id_list:
            item = Items.objects.filter(pk=item_id).first()
            items.append(item)
            sum += item.price
        client = Client.objects.filter(pk=client_id).first()
        order = Order(
            client=client,
            total=sum
        )
        order.save()
        for item in items:
            order.items.add(item)

        self.stdout.write(f'{order}')




