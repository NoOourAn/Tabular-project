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
timeslotss = None
timeslot = None
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
    if request.method == 'POST':
        global timeslotss
        global timeslot

        timeslotss=[]
        timeslot = []
        no_of_time_slots =None
        end_date=None
        second_exam_start_date=None
        second_exam_end_date=None
        third_exam_start_date=None
        third_exam_end_date=None


        numberofexams =request.POST['numberofexams']
        numberofexamsperday =request.POST['numberofexamsperday']
        thefirstexamstartdate =request.POST['thefirstexamstartdate']
        thegaptimebetweentheexams =request.POST['thegaptimebetweentheexams']
        # examduration =request.POST['examduration']
        examduration="03:00 AM"

        numberofexams= int(numberofexams)
        numberofexamsperday =int(numberofexamsperday)
        print(numberofexams)
        print(numberofexamsperday)


        no_of_time_slots = numberofexams
        the_first_exam_start_date=thefirstexamstartdate

        if numberofexamsperday >= 1:
            end_date=the_first_exam_start_date+examduration
            if numberofexamsperday >= 2:
                second_exam_start_date = end_date + thegaptimebetweentheexams
                second_exam_end_date = end_date + examduration
                if numberofexamsperday == 3:
                    third_exam_start_date = second_exam_end_date + thegaptimebetweentheexams
                    third_exam_end_date = second_exam_end_date + examduration


        for x in range(1,no_of_time_slots):
            if numberofexamsperday == 1:
                timeslot = []
                timeslot = [x, the_first_exam_start_date, end_date]

            if numberofexamsperday == 2:
                timeslot = []
                timeslot = [x,the_first_exam_start_date, end_date]
                timeslotss.append(timeslot)
                timeslot = []
                timeslot = [x,second_exam_start_date, second_exam_end_date]
                timeslotss.append(timeslot)

            if numberofexamsperday == 3:
                timeslot = []
                timeslot = [x, the_first_exam_start_date, end_date]
                timeslotss.append(timeslot)
                timeslot = []
                timeslot = [x, second_exam_start_date, second_exam_end_date]
                timeslotss.append(timeslot)
                timeslot = []
                timeslot = [x, third_exam_start_date, third_exam_end_date]
                timeslotss.append(timeslot)
        print(timeslotss)




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