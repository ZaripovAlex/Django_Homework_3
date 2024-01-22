import datetime
from django.http import HttpResponse
from django.shortcuts import render

from .models import Client, Order


# Create your views here.

def index(request):
    return HttpResponse('Hello World')
def get_all_orders(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client).all()
    context = {
        'client': client,
        'orders': orders
    }
    return render(request, 'hw1_app/all_orders.html', context=context)

def get_items(request, client_id):
    client = Client.objects.filter(pk=client_id).first()
    orders = Order.objects.filter(client=client).all()
    date=datetime.datetime.now()
    year = date - datetime.timedelta(years=1)
    year_items = ()
    month = date - datetime.timedelta(months=1)
    month_items = ()
    week = date - datetime.timedelta(weeks=1)
    week_items = ()
    for order in orders:
        if order.date>= year:
            for item in order.items.all():
                year_items.append(item)
        elif order.date>= month:
            for item in order.items.all():
                month_items.append(item)
        elif order.date>= week:
            for item in order.items.all():
                week_items.append(item)

    context = {
        'client': client,
        'year': list(year_items),
        'month': list(month_items),
        'week': list(week_items),

    }

    return render(request, context=context,template_name='hw1_app/all_items.html')
