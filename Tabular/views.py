from django.shortcuts import render ,get_object_or_404
from services.models import Timetables



def home(request):
    return render(request, 'home.html')


def student(request):
    return render(request, 'student-home.html')


def about(request):
    return render(request, 'about.html')

from services import TimeTable

def search(request):
    if request.method == 'POST':
        code = request.POST['search']
        try:
            # table = Timetables.objects.get(pk=code)
            table = Timetables.objects.get(accessCode=code)
            # table = get_object_or_404(Timetables , pk=code)

            print("menemenemenemenmenpppppppp")
            print(table)
            timeslots = TimeTable.get_timeslots()
            timeslots.sort
            tt = table.exams
            print(tt)
            subjects = {}
            for i in tt:
                if i[4] not in timeslots:
                    timeslots.append(i[4])
                if i[3] in subjects:
                    templist = subjects[i[3]]
                    templist[i[4]] = [i[0], i[1], i[2]]
                    subjects[i[3]] = templist
                else:
                    templist = {i[4]: [i[0], i[1], i[2]]}
                    subjects[i[3]] = templist
            return render(request, 'student-home.html',
                          {'code':code, 'tt': tt,'timeslots': timeslots, 'subjects': subjects})

            # if table is not None:
            # return render(request,'student-home.html',{'code':code , 'table':table})
        except Timetables.DoesNotExist:
            # elif table.DoesNotExist:
            return render(request, 'student-home.html',{'error':'not valid'})
    else:
        return render(request, 'student-home.html')





