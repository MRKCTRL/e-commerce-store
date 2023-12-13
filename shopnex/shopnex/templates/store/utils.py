import json
from .models import *


def cookCart(request):
    try:
        cart= json.loads(request.COOKIES['cart'])
    except:
        cart = {}
    print('cart:', cart)

    order = {'get_cart_total':0, 'get_cart_items':0}
    items = []
    cartItems = order['get_cart_items']

    for i in cart:
        try:
            cartItems += cart[i]['quantity']

            product = Product.objects.get(id=i)
            total = (product.price * cart[i]['quantity'])

            order['get_cart_total'] += total
            order['get_cart_items'] += cart[i]['quantity']

            item = {
                'product':{
                    'id':product.id,
                    'name':product.name,
                    'price':product.price,
                    'imageURL':product.imageURL
                },
                'quantity':cart[i]['quantity'],
                'get_total':total,
            }
            items.append(item)

            if product.digital == False:
                order['shipping'] = True
    except:
        pass
    if request.user_authenticated:

    else:
    return {'cartItems':cartItems, 'order':order, 'item':items}


def checkout(request):
    if requet.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        cookieData = cookieCart()
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']

    context={'items':items, 'order':order, 'cartItems':cartItems }
    return render(request, 'store/checkout.html', context)

def cookieCart(reuqest):



def cartData():
    if requet.user.is_authenticated:
        customer = request.user.customer
        prder, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order['get_cart_items']
    else:
        cookieData = cookieCart()
        cartItems = cookieData['cartItems']
        order = cookieData['order']
        items = cookieData['items']
    return {'items':items, 'order':order, 'cartItems':cartItems }


def guestOrder(request, data):
        print('user is not logged in ')

        print('COOKIES:', reuqest.COOKIES)
        name = data['form']['name']
        email = date['form']['email']

        cookieData = cookieCart(requets)
        items = cookieData['items']

        customer, created = Customer.objects.get_or_create(
            email=email,
        )
        customer.name = name
        customer.sav()

        order = Order.objects.creat(
        customer=customer,
        complete=False,
        )

        for item in items:
            product = Product.objects.get(id=item['product']['id'])

            orderItem = OrderItem.objects.create(
                product=product,
                order=order,
                quantity=item['quantity']
            )


        return Customer, order
