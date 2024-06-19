from django.shortcuts import HttpResponse

# Create your views here.
def home(requests):
    return HttpResponse("Hello, this is an internet appliation!")