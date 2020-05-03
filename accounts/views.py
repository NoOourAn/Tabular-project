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
                return render(request,'accounts/signupp.html' , {'error':'username has already taken'})
            except Account.DoesNotExist:
                user =  Account.objects.create_user(username= request.POST['username'],email=request.POST['email'], password=request.POST['password'], cc='0',univ=request.POST['univ'],faculty=request.POST['faculty'],gender=request.POST['gender'],age=request.POST['age'],level=request.POST['level'],is_S=True,is_U=False)
                auth.login(request,user)
                return redirect('student')
        else:
            return render(request, 'accounts/signupp.html', {'error': 'PASSWORD MUST MATCH '})

    else:

        return render (request,'accounts/signupp.html')

def osignup (request):
    if request.method == 'POST' :

        if request.POST['password'] ==request.POST['password2']:
            try:
                user = Account.objects.get(username=request.POST['username'],email=request.POST['email'],univ=request.POST['univ'],faculty=request.POST['faculty'],)
                return render(request,'accounts/signupoo.html' , {'error':'username or email has already taken'})
            except Account.DoesNotExist:
                user =  Account.objects.create_user(username= request.POST['username'],email=request.POST['email'], password=request.POST['password'], cc=request.POST['cc'],univ=request.POST['univ'],faculty=request.POST['faculty'],gender='x',age='0',level='0',is_S=False,is_U=True)
                auth.login(request,user)
                return redirect('manualdata')
        else:
            return render(request, 'accounts/signupoo.html', {'error': 'PASSWORD MUST MATCH '})

    else:

        return render (request,'accounts/signupoo.html')




def login(request):
    if request.method == 'POST' :
        user = authenticate(username=request.POST['username'],password =request.POST['password'])
        if user is not None:
            loogin(request,user)
            if request.user.is_U:
                return redirect('manualdata')
            else:
                return redirect('student')
        else:
            return render(request, 'accounts/login.html',{'error':'username or password is not correct m3 enohom correcr'})
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('home')

def reg(request):
   return render(request,'accounts/reg.html')

def reg2(request):
   return render(request, 'accounts/reg2.html')

def o(request):
   return render(request,'accounts/osignup.html')

def signupp(request):
   return render(request,'accounts/signupp.html')

def signupoo(request):
   return render(request,'accounts/signupoo.html')




