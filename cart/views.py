from django.shortcuts import render, redirect
from store.models import Product
# Create your views here.
from .models import Cart, CartItem


def cart(request):
    return render(request, 'cart/cart.html')


def add_to_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart_id = request.session.session_key
    cart = Cart.objects.create(
        cart_id=cart_id
    )
    cart.save()
    cart_item = CartItem.objects.create(
        product=product,
        quantity=1,
        cart=cart
    )
    cart_item.save()
    return redirect('cart')
