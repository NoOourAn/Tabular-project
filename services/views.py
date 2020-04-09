from django.shortcuts import render , get_object_or_404, redirect
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from .models import Timetables
from django.http import HttpResponse
from services.utils import render_to_pdf

from services import TimeTable

to_pdf = []
startdate = None
duedate = None
noofexams = None
timeslots = None
studentdb = None
subjectdb = None
roomdb = None


def home(request):
    return render(request, 'services/home.html')

def step1(request):
    return render(request, 'services/manual-data.html')

def step2(request):
    if request.method == 'POST':
        global startdate,duedate,noofexams
        startdate = request.POST['startdate']
        duedate = request.POST['duedate']
        noofexams = request.POST['examsNo']

    print(startdate)
    print(duedate)
    print(noofexams)
    return render(request, 'services/timeslots.html')

def step3(request):
    if request.method == 'POST':
        global timeslots
        timeslots = request.POST['myInputs[]']

    print(timeslots)
    return render(request , 'services/excel-sheet.html')

# def step3(request, tt_id):
#     timetable = get_object_or_404(Timetables , accessCode = tt_id)
#     return render(request, 'services/generated-timetable.html' ,{'tt':timetable})

def step4(request):
    if request.method == 'POST':
        global studentdb,roomdb,subjectdb
        doc = request.FILES  # returns a dict-like object
        studentdb = doc['st-db']
        subjectdb = doc['sub-db']
        roomdb = doc['rm-db']

    print(studentdb)
    print(subjectdb)
    print(roomdb)
    return render(request, 'services/generated-timetable.html')

from services import dbconvert

# assign = dbconvert.assign_filename()

def boom(request):
    dbconvert.fetch_data.assign.set_StudentsFilename(studentdb)
    dbconvert.fetch_data.assign.set_SubjectsFilename(subjectdb)
    dbconvert.fetch_data.assign.set_RoomsFilename(roomdb)
    print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
    print(dbconvert.fetch_data.assign.get_SubjectsFilename())
    print(dbconvert.fetch_data.assign.get_StudentsFilename())
    print(dbconvert.fetch_data.assign.get_RoomsFilename())

    tt = TimeTable.generateTT()
    global to_pdf
    to_pdf = tt
    TT = Timetables()
    TT.startDate = startdate
    TT.dueDate = duedate
    # TT.orgId = "boom"
    # TT.accessCode = 1
    TT.exams = tt
    TT.save()
    subjects = {}
    for i in tt:
        # if i[4] not in timeslots:
        #     timeslots.append(i[4])
        if i[3] in subjects:
            templist = subjects[i[3]]
            templist[i[4]] = [i[0],i[1],i[2]]
            subjects[i[3]] = templist
        else:
            templist = {i[4]:[i[0],i[1],i[2]]}
            subjects[i[3]] = templist
    # timeslots = TimeTable.get_timeslots()
    # timeslots.sort
    # print(timeslots)
    print(subjects)

    return render(request, 'services/generated-timetable.html', {'success': 'hahahahahahahahaaaa', 'tt': tt , 'timeslots':timeslots, 'subjects':subjects})

def create_pdf(request):
    data = {
        'a': 'noura amora',
        'b': to_pdf,
        'c': 'baba samy <3 ',  #7aga htegi mn el auth
        'd': 1233434,
    }
    pdf = render_to_pdf('services/pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')