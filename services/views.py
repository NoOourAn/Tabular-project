from django.shortcuts import render

# Create your views here.
def step1(request):
    return render(request, 'services/manual-data.html')

def step2(request):
    return render(request , 'services/excel-sheet.html')

def step3(request):
    return render(request, 'services/generated-timetable.html')

def home(request):
    return render(request, 'services/home.html')
