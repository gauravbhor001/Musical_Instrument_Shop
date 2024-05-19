from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Instrument(models.Model):

    instrumentName = models.CharField(max_length=50)
    description = models.TextField()
    price = models.IntegerField()
    img = models.ImageField(upload_to='pics')


class Brands(models.Model):
    imges = models.ImageField(upload_to='pic')


class Cart(models.Model):
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)
    username = models.ForeignKey(User, on_delete=models.CASCADE)


class Order(models.Model):
    totalBill = models.IntegerField()
    order_date = models.DateField(auto_now=True)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
