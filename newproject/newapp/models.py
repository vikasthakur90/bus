from django.db import models

class Register(models.Model):
    first_name = models.CharField(max_length=50)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=15)
    email = models.CharField(max_length=30)

    def __str__(self):
        return "first_name:"+self.first_name+" username:"+self.username+" email:"+self.email

class Busdetails(models.Model):
    reg_no = models.CharField(max_length=10)
    source = models.CharField(max_length=20)
    destination = models.CharField(max_length=20)
    distance = models.IntegerField()
    type = models.CharField(max_length=30)
    available_seat = models.IntegerField()
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    d_time = models.TimeField(auto_now=False, auto_now_add=False)
    a_time = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        b = Busdetails.objects.all()
        return self.source

class Book(models.Model):
    BOOKED = 'B'
    CANCELLED = 'C'

    TICKET_STATUSES = ((BOOKED, 'Booked'),
                       (CANCELLED, 'Cancelled'),)
    email = models.EmailField()
    name = models.CharField(max_length=30)
    #userid =models.DecimalField(decimal_places=0, max_digits=2)
    busid=models.DecimalField(decimal_places=0, max_digits=2)
    bus_name = models.CharField(max_length=30)
    source = models.CharField(max_length=30)
    dest = models.CharField(max_length=30)
    nos = models.DecimalField(decimal_places=0, max_digits=2)
    price = models.DecimalField(decimal_places=2, max_digits=6)
    date = models.DateField()
    #time = models.TimeField()
    status = models.CharField(choices=TICKET_STATUSES, default=BOOKED, max_length=255)

    def __str__(self):
        return self.email