from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'orders/index.html')


def orders(request):
    return render(request, 'orders/order.html')

