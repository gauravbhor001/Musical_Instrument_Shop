from django.urls import path

from Accounts import views

urlpatterns = [
    path('register', views.createUser, name='createUser'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('index', views.index, name='index'),



]