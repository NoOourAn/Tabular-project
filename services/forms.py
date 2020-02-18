from django import forms

FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

INTEGER_CHOICES= [tuple([x,x]) for x in range(0,24)]

class ManualData(forms.Form):
    startdate = forms.DateField(label='Start Date ',)
    duedate = forms.DateField(label='Start Date ',)

class TimeSlots(forms.Form):
    days = forms.IntegerField(label='Day ', widget=forms.Select(choices=FRUIT_CHOICES))
    timeslot = forms.IntegerField(label="TimeSlot", widget=forms.Select(choices=INTEGER_CHOICES))

class ExcelSheet(forms.Form):
    courses = forms.FileField()
    students = forms.FileField()
