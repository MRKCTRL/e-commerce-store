from django.shortcuts import render
from django.contrib import admin
from .models import *

def store(request):
    producs = Products.object.all()
    context={'products':products}
    return render(request, 'store/store.html', context)

def checkout(request):
    if requet.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items'}

    context={'items':items, 'order':order}
    return render(request, 'store/checkout.html', context)

def cart(request):
    context={}
        def checkout(request):
            if requet.user.is_authenticated:
                customer = request.user.customer
                prder, created = Order.objects.get_or_create(customer=customer, complete=False)
                items = order.orderitem_set.all()
            else:
                order = {'get_cart_total':0, 'get_cart_items':0}
                items = []
            context = {'items':items, 'order':order}
    return render(request, 'store/cart.html', context)

def index(request):
    context={}
    return render(request, 'store/index.html', context)
