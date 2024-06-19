from django.shortcuts import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(requests):
    return render(requests, 'index.html')

