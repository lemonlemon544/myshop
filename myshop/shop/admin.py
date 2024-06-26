from django.contrib import admin
from .models import Product

class Product_Admin(admin.ModelAdmin):
    pass

# Register your models here.
admin.site.register(Product, Product_Admin)
