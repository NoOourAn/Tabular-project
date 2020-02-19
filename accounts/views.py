from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib  import auth
from .models import Account
from django.contrib.auth import authenticate, login as loogin





def signup (request):
    if request.method == 'POST' :

        if request.POST['password'] ==request.POST['password2']:
            try:
                user = Account.objects.get(username=request.POST['username'],email=request.POST['email'],)
                return render(request,'accounts/signup.html' , {'error':'username has already taken'})
            except Account.DoesNotExist:
                user =  Account.objects.create_user(username= request.POST['username'],email=request.POST['email'], password=request.POST['password'], cc='0',univ=request.POST['univ'],faculty=request.POST['faculty'],gender=request.POST['gender'],age=request.POST['age'],level=request.POST['level'])
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
                user = Account.objects.get(username=request.POST['username'],email=request.POST['email'],univ=request.POST['univ'],faculty=request.POST['faculty'],)
                return render(request,'accounts/signup.html' , {'error':'username or email has already taken'})
            except Account.DoesNotExist:
                user =  Account.objects.create_user(username= request.POST['username'],email=request.POST['email'], password=request.POST['password'], cc=request.POST['cc'],univ=request.POST['univ'],faculty=request.POST['faculty'],gender='x',age='0',level='0')
                auth.login(request,user)
                return redirect('home')
        else:
            return render(request, 'accounts/osignup.html', {'error': 'PASSWORD MUST MATCH '})

    else:

        return render (request,'accounts/osignup.html')




def login(request):
    if request.method == 'POST' :
        user = authenticate(username=request.POST['username'],password =request.POST['password'])
        if user is not None:
            loogin(request,user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is not correct m3 enohom correcr'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('home')

