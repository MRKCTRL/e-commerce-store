from django.shortcuts import render
from django.contrib import admin
from .models import *
from django.http import JsonResponse
import datetime

def store(request):
    if requet.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0}
        cartItems = order['get_cart_items']

    producs = Products.object.all()
    context={'products':products, 'cartItems':cartItems}
    return render(request, 'store/store.html', context)

def checkout(request):
    if requet.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total':0, 'get_cart_items':0, 'shipping':False}
        cartItems = order['get_cart_items']

    context={'items':items, 'order':order, 'cartItems':cartItems }
    return render(request, 'store/checkout.html', context)

def cart(request):
    context={}
        def checkout(request):
            if requet.user.is_authenticated:
                customer = request.user.customer
                prder, created = Order.objects.get_or_create(customer=customer, complete=False)
                items = order.orderitem_set.all()
                cartItems = order['get_cart_items']
            else:
                order = {'get_cart_total':0, 'get_cart_items':0}
                items = []
                cartItems = order['get_cart_items']


            context = {'items':items, 'order':order, 'cartItems':cartItems }
    return render(request, 'store/cart.html', context)

def index(request):
    context={}
    return render(request, 'store/index.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)


    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)

def proccessOder(request):
    # print('Data:', request.body)
    transaction_id = datetime.datetime.now().timestamp()
    data = json.load(request.body)
    if request.user.is_authenticated:
        customer = request.user.Customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        total = data['from']['total']
        order.transaction_id = transaction_id

        if total == order.get_cart_total:
            order.complete = True
        order.save()

        if order.shipping == True:
            ShippingAddress.objects.create(
            customer=customer,
            order=order,
            address=data['shipping']['address'],
            city=data['shipping']['city'],
            province=data['shipping']['province'],
            zipcode=data['shipping']['zipcode'],
            )
    return JsonResponse('payment complete', safe=False)
