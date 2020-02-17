from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib  import auth
from .models import Account





def signup (request):
    if request.method == 'POST' :

        if request.POST['password'] ==request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request,'accounts/signup.html' , {'error':'username has already taken'})
            except User.DoesNotExist:
                user =  User.objects.create_user(request.POST['username'], password=request.POST['password'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html', {'error': 'PASSWORD MUST MATCH '})

    else:

        return render (request,'accounts/signup.html')

def osignup (request):
    if request.method == 'POST' :

        if request.POST['password'] ==request.POST['password2']:
            try:
                user = Account.objects.get(username=request.POST['username'],email=request.POST['email'])
                return render(request,'accounts/signup.html' , {'error':'username or email has already taken'})
            except Account.DoesNotExist:
                user =  Account.objects.create_user(email=request.POST['email'],username= request.POST['username'], password=request.POST['password'], cc=request.POST['cc'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/osignup.html', {'error': 'PASSWORD MUST MATCH '})

    else:

        return render (request,'accounts/osignup.html')


def home(request):
    return render(request, 'accounts/home.html')


def login(request):
    if request.method == 'POST' :
        user = auth.authenticate(username=request.POST['username'],password =request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is not correct'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('home')

