from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('/get_order/<int:client_id>', views.get_all_orders, name='orders'),
    path('/get_items/<int:client_id>', views.get_items, name='items'),
]



