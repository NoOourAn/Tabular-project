from django.shortcuts import render , get_object_or_404, redirect
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from .models import Timetables
from django.http import HttpResponse
from services.utils import render_to_pdf
import openpyxl
from services import TimeTable
from services import dbconvert

to_pdf = []
startdate = None
duedate = None
noofexams = None
timeslotss = [[1, "09:00 - 10:00", "SUNDAY" , "1/1"],
             [2, "10:00 - 11:00", "SUNDAY" , "1/1"],
             [3 , "11:00 - 12:00", "SUNDAY" , "1/1"],
             [4 , "09:00 - 10:00", "SUNDAY" , "8/1"],
             [5 , "10:00 - 11:00", "SUNDAY" , "8/1"],
             [6 , "11:00 - 12:00", "SUNDAY" , "8/1"],
             [7 , "09:00 - 10:00", "SUNDAY" , "15/1"],
             [8 , "10:00 - 11:00", "SUNDAY" , "15/1"],
             [9 , "11:00 - 12:00", "SUNDAY" , "15/1"],
             [10 , "09:00 - 10:00", "SUNDAY" , "22/1"],
             [11 , "10:00 - 11:00", "SUNDAY" , "22/1"],
             [12 , "11:00 - 12:00", "SUNDAY" , "22/1"],
             [13 , "09:00 - 10:00", "MONDAY" , "2/1"],
             [14 , "10:00 - 11:00", "MONDAY" , "2/1"],
             [15 , "11:00 - 12:00", "MONDAY" , "2/1"],
             [16 , "09:00 - 10:00", "MONDAY" , "9/1"],
             [17 , "10:00 - 11:00", "MONDAY" , "9/1"],
             [18 , "11:00 - 12:00", "MONDAY" , "9/1"],
             [19 , "09:00 - 10:00", "MONDAY" , "16/1"],
             [20 , "10:00 - 11:00", "MONDAY" , "16/1"],
             [21 , "11:00 - 12:00", "MONDAY" , "16/1"],
             [22 , "09:00 - 10:00", "MONDAY" , "23/1"],
             [23 , "10:00 - 11:00", "MONDAY" , "23/1"],
             [24 , "11:00 - 12:00", "MONDAY" , "23/1"],
             [25 , "09:00 - 10:00", "TUESDAY" , "3/1"],
             [26 , "10:00 - 11:00", "TUESDAY" , "3/1"],
             [27 , "11:00 - 12:00", "TUESDAY" , "3/1"],
             [28 , "09:00 - 10:00", "TUESDAY" , "10/1"],
             [29 , "10:00 - 11:00", "TUESDAY" , "10/1"],
             [30 , "11:00 - 12:00", "TUESDAY" , "10/1"],
             [31 , "09:00 - 10:00", "TUESDAY" , "17/1"],
             [32 , "10:00 - 11:00", "TUESDAY" , "17/1"],
             [33 , "11:00 - 12:00", "TUESDAY" , "17/1"],
             [34 , "09:00 - 10:00", "TUESDAY" , "24/1"],
             [35 , "10:00 - 11:00", "TUESDAY" , "24/1"],
             [36 , "11:00 - 12:00", "TUESDAY" , "24/1"],
             [37 , "09:00 - 10:00", "WEDNSDAY" , "4/1"],
             [38 , "10:00 - 11:00", "WEDNSDAY" , "4/1"],
             [39 , "11:00 - 12:00", "WEDNSDAY" , "4/1"],
             [40 , "09:00 - 10:00", "WEDNSDAY" , "11/1"],
             [41 , "10:00 - 11:00", "WEDNSDAY" , "11/1"],
             [42 , "11:00 - 12:00", "WEDNSDAY" , "11/1"],
             [43 , "09:00 - 10:00", "WEDNSDAY" , "18/1"],
             [44 , "10:00 - 11:00", "WEDNSDAY" , "18/1"],
             [45 , "11:00 - 12:00", "WEDNSDAY" , "18/1"],
             [46 , "09:00 - 10:00", "WEDNSDAY" , "25/1"],
             [47 , "10:00 - 11:00", "WEDNSDAY" , "25/1"],
             [48 , "11:00 - 12:00", "WEDNSDAY" , "25/1"],
             [49 , "09:00 - 10:00", "THURSDAY" , "5/1"],
             [50 , "10:00 - 11:00", "THURSDAY" , "5/1"],
             [51 , "11:00 - 12:00", "THURSDAY" , "5/1"],
             [52 , "09:00 - 10:00", "THURSDAY" , "12/1"],
             [53 , "10:00 - 11:00", "THURSDAY" , "12/1"],
             [54 , "11:00 - 12:00", "THURSDAY" , "12/1"],
             [55 , "09:00 - 10:00", "THURSDAY" , "19/1"],
             [56 , "10:00 - 11:00", "THURSDAY" , "19/1"],
             [57 , "11:00 - 12:00", "THURSDAY" , "19/1"],
             [58 , "09:00 - 10:00", "THURSDAY" , "26/1"],
             [59 , "10:00 - 11:00", "THURSDAY" , "26/1"],
             [60 , "11:00 - 12:00", "THURSDAY" , "26/1"]]
studentdb = None
subjectdb = None
roomdb = None
wb = None


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
    #if request.method == 'POST':
        #global timeslotss
        #timeslotss = request.POST['myInputs[]']

    #print(timeslotss)
    return render(request , 'services/excel-sheet.html')

# def step3(request, tt_id):
#     timetable = get_object_or_404(Timetables , accessCode = tt_id)
#     return render(request, 'services/generated-timetable.html' ,{'tt':timetable})

def step4(request):
    if request.method == 'POST':
        global studentdb,roomdb,subjectdb,wb
        doc = request.FILES  # returns a dict-like object
        studentdb = openpyxl.load_workbook(doc['st-db'])
        subjectdb = openpyxl.load_workbook(doc['sub-db'])
        roomdb = openpyxl.load_workbook(doc['rm-db'])
    return render(request, 'services/generated-timetable.html')

from services import dbconvert

# assign = dbconvert.assign_filename()

def boom(request):
    dbconvert.fetch_data.assign.set_StudentsFile(studentdb)
    dbconvert.fetch_data.assign.set_SubjectsFile(subjectdb)
    dbconvert.fetch_data.assign.set_RoomsFile(roomdb)
    dbconvert.fetch_data.assign.set_TimeSlots(timeslotss)
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
    timeslots = TimeTable.get_timeslots()
    timeslots.sort
    subjects = {}
    for i in tt:
        if i[4] not in timeslots:
            timeslots.append(i[4])
        if i[3] in subjects:
            templist = subjects[i[3]]
            templist[i[4]] = [i[0],i[1],i[2]]
            subjects[i[3]] = templist
        else:
            templist = {i[4]:[i[0],i[1],i[2]]}
            subjects[i[3]] = templist
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