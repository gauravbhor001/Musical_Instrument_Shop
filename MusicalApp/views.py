from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

# Create your views here.
from MusicalApp.models import Instrument, Brands, Cart, Order


def index(request):
    details = Instrument.objects.all()
    data = Brands.objects.all()
    d = {'details': details, 'data': data}
    return render(request, "index.html", d)


def addToCart(request, id):
    uid = request.session.get('uid')
    c = Cart()
    product = Instrument.objects.get(id=id)
    user = User.objects.get(id=uid)
    c.instrument = product
    c.username = user
    c.save()
    messages.info(request, 'Cart added successfully')
    return redirect("/")


def cartlist(request):
    uid = request.session.get('uid')
    cr = Cart.objects.filter(username=uid)
    cl = Instrument.objects.all()
    if request.method == 'POST':
        totalbill = 0
        qty = request.POST['qty']

        for i in cr:
            totalbill = totalbill + i.instrument.price * int(qty)

        o = Order()
        o.totalBill = int(totalbill)
        o.username = User.objects.get(id=uid)
        o.save()
        for i in cr:
            i.delete()

        return render(request, "index.html", {'totalbill': totalbill})
    else:

        for i in cr:
            d = {'cr': cr, 'cl': cl}
        return render(request, 'cartlist.html', d)


def Products(request):
    return render(request, 'products.html')
