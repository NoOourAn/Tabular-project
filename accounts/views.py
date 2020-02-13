from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib  import auth



def home(request):
    return    render(request, 'accounts/home.html')



def login(request):
     return render(request, 'accounts/login.html')


def logout(request):
    return    render(request, 'accounts/logout.html')




def signup (request):
    if request.method == 'POST' :

        if request.POST['password'] ==request.POST['password2']:
            try:
                    user = User.objects.get(username=request.POST['username'])
                    return render (request,'accounts/signup.html' , {'error':'username has already taken'})
            except User.DoesNotExist:
                      user =  User.objects.create_user(request.POST['username'], password=request.POST['password'])
                      auth.login(request,user)
            return redirect('home')
    else:

            return render (request,'accounts/signup.html')

