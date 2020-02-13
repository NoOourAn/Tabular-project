from django import forms

class ManualData(forms.Form):
    startdate = forms.DateField()
    duedate = forms.DateField()

class TimeSlots(forms.Form):
    days = forms.IntegerField()
    timeslot = forms.IntegerField()

class ExcelSheet(forms.Form):
    students = forms.FileField()
    courses = forms.FileField()