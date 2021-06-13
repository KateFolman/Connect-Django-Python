from .models import OrderDetail
from django.shortcuts import render


def index(request):
    orderss = OrderDetail.objects.all()
    return render(request, 'orders/index.html', {'title': 'Главная страница сайта', 'order' : orderss})


def orders(request):
    return render(request, 'orders/order.html')

