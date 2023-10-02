from django.shortcuts import render
from .models import Product
# Create your views here.


def store(request):
    products = Product.objects.filter(is_available=True)
    return render(request, 'store/store.html', {'products': products})


def product_detail(request):
    return render(request, 'store/product-detail.html')
