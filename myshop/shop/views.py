from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(requests):
    products = Product.objects.all()

    return render(requests, "index.html", {
        'products': products
    })
