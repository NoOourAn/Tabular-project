from django import forms
from datetime import date ,timedelta
from django import utils
# from multivaluefield import MultiValueField
from django.forms.fields import MultiValueField

# FRUIT_CHOICES= [
#     ('orange', 'Oranges'),
#     ('cantaloupe', 'Cantaloupes'),
#     ('mango', 'Mangoes'),
#     ('honeydew', 'Honeydews'),
#     ]

# INTEGER_CHOICES= [tuple([x,x]) for x in range(0,24)]

def return_date_time():
    now = utils.timezone.now()
    return now + timedelta(days=7)

def default_start_time():
    now = utils.timezone.now()
    start = now.replace(hour=9, minute=0 , second=0)
    return start

def default_end_time():
    now = utils.timezone.now()
    end = now.replace(hour=12, minute=0, second=0)
    return end

class ManualData(forms.Form):
    startdate = forms.DateField(label='Start Date ',initial=date.today().strftime("%Y-%m-%d"))
    duedate = forms.DateField(label='Start Date ',initial=return_date_time)

class TimeSlots(forms.Form):
    # days = forms.IntegerField(label='Day ', widget=forms.Select(choices=FRUIT_CHOICES))
    examstartime = forms.TimeField(label="Exam Start Time",initial=default_start_time)
    examduetime = forms.TimeField(label="Exam Due Time",initial=default_end_time)
    # emails = MultiValueField(forms.TimeField, "Time")


class ExcelSheet(forms.Form):
    courses = forms.FileField()
    students = forms.FileField()
