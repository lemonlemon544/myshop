from django.http import HttpResponse
from django.shortcuts import render

from .models import Product

# Create your views here.

def home(request):
    search = request.GET.get('search')

    products = Product.objects.all()

    products = Product.objects.all()
    if search:
        products = Product.objects.filter(name__contains=search).all()
    else:
        products = Product.objects.all()

    return render(request, "index.html", {
        'products': products,
        'search': search,
    })

def view_product(request, id):
    product = Product.objects.filter(id=id).first()
    return render(request, 'product.html', {
        'product': product
    })