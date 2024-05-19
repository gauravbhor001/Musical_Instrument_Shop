from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from MusicalApp.models import Cart


def createUser(request):
    if request.method == 'POST':
        fname = request.POST['firstName']
        lname = request.POST['lastName']
        username = request.POST['UserName']
        email = request.POST['emailId']
        pass1 = request.POST['Pass1']
        pass2 = request.POST['Pass2']
        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                # print("Username already exist")
                messages.info(request, "Username already exist")
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                # print("EmailId already exist")
                messages.info(request, "EmailId already exist")
                return render(request, 'register.html')
            else:
                u = User.objects.create_user(first_name=fname, last_name=lname, username=username, email=email,
                                             password=pass1)
                u.save()
                # print('user created')
                messages.info(request, "You have successfully Registered")
                return redirect("/")
        else:
            # print("Password not matching")
            messages.info(request, "Password not matching")
            return render(request, "register.html")
    else:
        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            request.session['uid'] = user.id
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Login failed")
            return render(request, 'login.html')
    else:

        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect("/")


def index(request):
    return render(request, 'index.html')