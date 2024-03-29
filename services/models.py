from django.db import models
from datetime import date , timezone ,timedelta
from django import utils
from django.contrib.auth.models import User
from Tabular import settings

# Create your models here.


class Timetables(models.Model):

    def return_date_time():
        now = utils.timezone.now()
        return now + timedelta(days=7)

    # def save(self, *args, **kwargs):
    #     if not self.accessCode:
    #         self.accessCode = self.orgId + '-' + self.startDate + '-' + self.dueDate
    #     super().save(*args, **kwargs)

    def __str__(self):
        return self.accessCode

    def exams_as_list(self):
        return self.exams.split(' ')

    def subjects_as_list(self):
        exams = self.exams.split(' ')
        subjects = []
        for exam in exams:
            subjects.append(exam.split(',')[0])
        return subjects

    def rooms_as_list(self):
        exams = self.exams.split(' ')
        rooms = []
        for exam in exams:
            rooms.append(exam.split(',')[1])
        return rooms

    def fetch_data(code):
        table = Timetables(accessCode=code)
        return table.objects






    startDate = models.DateField(default=date.today)  #editable=False
    dueDate = models.DateField(default=return_date_time)   #editable=False
    exams = models.TextField(default='' )  #exam[dept,course,room,instructor-id,timeslot-id,no of students]  / #editable=False
    accessCode = models.TextField(default='' , primary_key=True)  #editable=False
    org = models.ForeignKey(settings.AUTH_USER_MODEL , on_delete= models.CASCADE)   #forign key mn table el accounts(organisations)/one(org) to many(timetables)/one(timetable) to one(org) / editable = False
    time_slots = models.TextField(default='' )
    def __str__(self):
        return self.accessCode

