from django.contrib import admin
from django.urls import path
from game import views
urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("products",views.products, name='products'),
    path("contact",views.contact, name='contact'),
]
