from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('contact', views.contact, name = 'contact'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('booking', views.booking, name='booking'),
    path('logout', views.logout, name='logout'),
    path('profile', views.profile, name='profile'),
]
