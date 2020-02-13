from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib  import auth



def home(request):
    return    render(request, 'accounts/home.html')

def signup (request):
    return render (request,'accounts/signup.html')


def login(request):
     return render(request, 'accounts/login.html')


def logout(request):
    return    render(request, 'accounts/logout.html')


