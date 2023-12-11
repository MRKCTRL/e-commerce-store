from django.urls import path, include
from . import views
from .views import index


urlpatterns = [
    path('', views.store, name="store"),
    path('index/', views.index, name="index"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
]
