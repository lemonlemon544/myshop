from django.shortcuts import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.
def home(requests):
    products = Product.objects.all()

    return render(requests, "index.html", {
        'products': products
    })

def view_product(request):
    return render(request, 'product.html')