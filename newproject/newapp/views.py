from django.http import HttpResponse
from .forms import UserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def login(request):

    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return render(request, 'profile.html')
        else:
            messages.success(request, 'invalid password')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


def booking(request):
    return render(request, 'booking.html')


def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.success(request,'USERNAME TAKEN')
                return render(request, 'register.html')
            elif User.objects.filter(email=email).exists():
                messages.success(request,'email already taken')
                return render(request, 'register.html')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name,
                                            last_name=last_name)
                user.save();
                return render(request, 'login.html')
        else:
            messages.success(request,'password not matched')
            return render(request, 'register.html')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return render(request, 'index.html')

def profile(request):
    return render(request, 'profile.html')