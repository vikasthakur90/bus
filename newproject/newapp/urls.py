from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
    path('bookings', views.bookings, name='bookings'),
    path('seebookings', views.seebookings, name = 'seebookings'),
    path('cancellings', views.cancellings, name = 'cancellings'),
]
