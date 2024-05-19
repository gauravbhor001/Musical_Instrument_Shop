from django.urls import path

from MusicalApp import views

urlpatterns = [
    path('', views.index, name='home'),
    path('addToCart/<int:id>', views.addToCart, name='addToCart'),
    path('cartlist', views.cartlist, name='cartlist'),
    path('Products', views.Products, name='Products'),
]
