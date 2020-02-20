from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def student(request):
    return render(request, 'student-home.html')


def about(request):
    return render(request, 'about.html')
