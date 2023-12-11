from django.db import models
from django.contrib.auth.models import User

class Custumer(models.Model):
    user = moduls.OneToOneField(User, on_delete=models.CASCADE null=True, blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
        # self.arg = arg

        def __str__(self):
            return self.name

class Product(Models.Model):
    name = models.Charfield(max_length=200)
    price = models.FloatField()
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

        def __str__(self):
            return self.name

        @property
        def imageURL(self):
            try:
                url = self.image.url
            except:
                url = ''
            return url

class Order(self):
    customer = models.ForiegnKey(Customer, on_delete=models.SET_NULL, null=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default=False,)
    transaction_id = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

class OrderItem(models.Model):
    product = models.ForiegnKey(Poduct, on_delete=models.SET_NULL, null=True)
    order = models.ForiegnKey(Order on_delete=models.SET_NULL, null=True)
    quantity = models.IntergField(defualt=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self quantity
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([items.quantity for item in orderitems])
        return total


class ShippingAddress(models.Model):
    customer = models.ForiegnKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForiegnKey(Order on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    province = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

        def __str__(self):
            return self.address
