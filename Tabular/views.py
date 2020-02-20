from django.shortcuts import render
from services.models import Timetables


def home(request):
    return render(request, 'home.html')


def student(request):
<<<<<<< HEAD
    return render(request, 'student-home.html')


def about(request):
    return render(request, 'about.html')
=======
    # accodes = request.GET['search']
    # print(accodes)
    # if request.method == 'POST':
    #     code = request.POST['search']
    #     # print(code)
    #     tables = Timetables.objects
    #     # return render(request,'student-home.html', {'tables':tables, 'code':code})
    #     return  HttpResponseRedirect(request,'student-home.html', {'tables':tables, 'code':code})

    if request.method == 'POST':
        code = request.POST['search']
        try:
            table = Timetables.objects.get(accessCode=code)
            # if table is not None:
            return render(request,'student-home.html',{'code':code , 'table':table})
        except Timetables.DoesNotExist:
            # elif table.DoesNotExist:
            return render(request, 'student-home.html',{'error':'not valid'})
    else:
        return render(request, 'student-home.html', {'m':'not validdd'})




>>>>>>> c285e37c0d85a53f95fad301e0350158016c8d6e
