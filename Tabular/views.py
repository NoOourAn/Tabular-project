from django.shortcuts import render
from services.models import Timetables

def home(request):
    return render(request,'home.html')
def student(request):
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
            return render(request,'student-home.html',{'code':code})
        except Timetables.DoesNotExist:
            # elif table.DoesNotExist:
            return render(request, 'student-home.html',{'error':'not valid'})
    else:
        return render(request, 'student-home.html', {'m':'not validdd'})




