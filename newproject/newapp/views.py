from django.http import HttpResponse
from .models import Book
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .admin import Busdetails


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


    if request.method== 'POST':
        source = request.POST['source']
        destination = request.POST['destination']
        if Busdetails.objects.filter(source=source):
            if Busdetails.objects.filter(destination=destination):
                b = Busdetails.objects.filter(source=source, destination=destination)
                bus = {
                    'obj': b
                    }
                return render(request,"busdetails.html", bus)
        else:
            messages.success(request, 'NO BUS AVAILABLE')


    return render(request, 'profile.html')

def bookings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        seats_r = int(request.POST.get('no_seats'))
        bus = Busdetails.objects.get(id=id_r)
        if bus:
            if bus.available_seat > int(seats_r):
                name_r = bus.reg_no
                cost = int(seats_r) * bus.price
                source_r = bus.source
                dest_r = bus.destination
                price_r = bus.price
                date_r = bus.date
                username_r = request.user.username
                email_r = request.user.email
                available_seat_r = bus.available_seat - seats_r
                Busdetails.objects.filter(id=id_r).update(available_seat=available_seat_r)
                book = Book.objects.create(name=username_r, email=email_r ,bus_name=name_r,
                                           source=source_r, busid=id_r,
                                           dest=dest_r, price=price_r, nos=seats_r, date=date_r,
                                           status='BOOKED')
                print('------------book id-----------', book.id)
                # book.save()
                return render(request, 'confirmation.html', locals())
            else:
                context["error"] = "Sorry select fewer number of seats"
                return render(request, 'busdetails.html', context)

    else:
        return render(request, 'busdetails.html')


def seebookings(request, new={}):
    context = {}
    id_r = request.user.email
    book_list = Book.objects.filter(email=id_r)
    if book_list:
        return render(request, 'booklist.html', locals())
    else:
        context["error"] = "Sorry no buses booked"
        return render(request, 'profile.html', context)

def cancellings(request):
    context = {}
    if request.method == 'POST':
        id_r = request.POST.get('bus_id')
        #seats_r = int(request.POST.get('no_seats'))

        try:
            book = Book.objects.get(id=id_r)
            bus = Busdetails.objects.get(id=book.busid)
            rem_r = bus.available_seat + book.nos
            Busdetails.objects.filter(id=book.busid).update(available_seat=rem_r)
            #nos_r = book.nos - seats_r
            Book.objects.filter(id=id_r).update(status='CANCELLED')
            Book.objects.filter(id=id_r).update(nos=0)
            return redirect(seebookings)
        except Book.DoesNotExist:
            context["error"] = "Sorry You have not booked that bus"
            return render(request, 'error.html', context)
    else:
        return render(request, 'profile.html')