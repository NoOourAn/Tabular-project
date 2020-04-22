from django.shortcuts import render, get_object_or_404, redirect
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
from .models import Timetables
from django.http import HttpResponse
from services.utils import render_to_pdf
import openpyxl
from services import TimeTable
from services import dbconvert
from datetime import datetime, timedelta

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
        global startdate, duedate, noofexams
        startdate = request.POST['startdate']
        duedate = request.POST['duedate']
        noofexams = request.POST['examsNo']

    print(startdate)
    print(duedate)
    print(noofexams)
    return render(request, 'services/timeslots.html')


def step3(request):
    if request.method == 'POST':

        numberofexams = request.POST['numberofexams']
        numberofexamsperday = request.POST['numberofexamsperday']

        numberofexams = int(numberofexams)
        numberofexamsperday = int(numberofexamsperday)

        ##########################################

        thefirstexamstartdate = request.POST['thefirstexamstartdate']
        thelastexamstartdate = request.POST['thelastexamstartdate']
        generalexamstarttime = request.POST['generalexamstarttime']
        generalexamendtime = request.POST['generalexamendtime']

        examduration_hrs = request.POST['examdurationH']
        examduration_min = request.POST['examdurationM']

        examduration_hrs = int(examduration_hrs)
        examduration_min = int(examduration_min)

        if examduration_hrs == 0:

            exdurationM_minus_15 = examduration_min - 15
            exdurationM_minus_30 = examduration_min - 30
            exdurationM_minus_45 = examduration_min - 45
            exdurationM_minus_60 = examduration_min - 60

            if exdurationM_minus_15 < 0:
                exdurationM_minus_15 *= -1
            if exdurationM_minus_30 < 0:
                exdurationM_minus_30 *= -1
            if exdurationM_minus_45 < 0:
                exdurationM_minus_45 *= -1
            if exdurationM_minus_60 < 0:
                exdurationM_minus_60 *= -1

            if exdurationM_minus_15 < exdurationM_minus_30 and \
               exdurationM_minus_15 < exdurationM_minus_45 and \
               exdurationM_minus_15 < exdurationM_minus_60:
                examduration_min = 15
                print(15)
            else:
                if exdurationM_minus_30 < exdurationM_minus_45 and \
                   exdurationM_minus_30 < exdurationM_minus_60:
                    examduration_min = 30
                    print(30)
                else:
                    if exdurationM_minus_45 < exdurationM_minus_60:
                        examduration_min = 45
                        print(45)
                    else:
                        examduration_min = 60
                        print(60)


        ##########################################

        thefirstexamstartdate = datetime.strptime(thefirstexamstartdate, "%Y-%m-%dT%H:%M")
        thelastexamstartdate = datetime.strptime(thelastexamstartdate, "%Y-%m-%dT%H:%M")
        generalexamstarttime = datetime.strptime(generalexamstarttime, "%H:%M")
        generalexamendtime = datetime.strptime(generalexamendtime, "%H:%M")

        print(thefirstexamstartdate)
        print(thelastexamstartdate)

        x = 1
        time_available = []

        while True:

            lastthefirstexamstartdate = thefirstexamstartdate
            thefirstexamstartdate += timedelta(hours=examduration_hrs, minutes=examduration_min)
            if thefirstexamstartdate.hour <= generalexamendtime.hour:
                time_available.append([x,
                                       lastthefirstexamstartdate.strftime("%H:%M")
                                       + " - "
                                       + thefirstexamstartdate.strftime("%H:%M"),
                                       lastthefirstexamstartdate.strftime("%A").upper(),
                                       lastthefirstexamstartdate.strftime("%d/%m")
                                       ])
                x += 1

            if thefirstexamstartdate.hour >= generalexamendtime.hour:
                # lw al youm antha 5o4 3la alyoum aly wrah
                thefirstexamstartdate += timedelta(days=1)
                thefirstexamstartdate = datetime(year=thefirstexamstartdate.year,
                                                 month=thefirstexamstartdate.month,
                                                 day=thefirstexamstartdate.day,
                                                 hour=generalexamstarttime.hour,
                                                 minute=generalexamstarttime.minute)

            if thefirstexamstartdate >= thelastexamstartdate:
                break

        print(time_available)

    return render(request, 'services/excel-sheet.html')


# def step3(request, tt_id):
#     timetable = get_object_or_404(Timetables , accessCode = tt_id)
#     return render(request, 'services/generated-timetable.html' ,{'tt':timetable})

def step4(request):
    if request.method == 'POST':
        global studentdb, roomdb, subjectdb, wb
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
            templist[i[4]] = [i[0], i[1], i[2]]
            subjects[i[3]] = templist
        else:
            templist = {i[4]: [i[0], i[1], i[2]]}
            subjects[i[3]] = templist
    return render(request, 'services/generated-timetable.html',
                  {'success': 'hahahahahahahahaaaa', 'tt': tt, 'timeslots': timeslots, 'subjects': subjects})


def create_pdf(request):
    data = {
        'a': 'noura amora',
        'b': to_pdf,
        'c': 'baba samy <3 ',  # 7aga htegi mn el auth
        'd': 1233434,
    }
    pdf = render_to_pdf('services/pdf.html', data)
    return HttpResponse(pdf, content_type='application/pdf')

# thefirstexamstartdate = datetime.strptime(thefirstexamstartdate, "%H:%M")
# print(type(thefirstexamstartdate))
#
# print("in H: " + str(thefirstexamstartdate.hour))
# print("in M: " + str(thefirstexamstartdate.minute))
#
# print(thefirstexamstartdate)
# print(thefirstexamstartdate + timedelta(hours=thefirstexamstartdate.hour, minutes=thefirstexamstartdate.minute))
#
# thefirstexamstartdate = thefirstexamstartdate.strftime("%H:%M")
# print(thefirstexamstartdate)
