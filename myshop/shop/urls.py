from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("product", views.view_product, name="view_product"),
    path("product/<int:id>", views.view_product, name="view_product")
]