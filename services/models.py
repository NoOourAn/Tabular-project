from django.db import models
from datetime import date , timezone ,timedelta
from django import utils

# Create your models here.
class Timetables(models.Model):
    def return_date_time():
        now = utils.timezone.now()
        return now + timedelta(days=7)

    def save(self, *args, **kwargs):
        if not self.accessCode:
            self.accessCode = self.orgId + '-' + self.startDate + '-' + self.dueDate
        super().save(*args, **kwargs)

    startDate = models.DateField(default=date.today)  #editable=False
    dueDate = models.DateField(default=return_date_time)   #editable=False
    exams = models.TextField(default='' )  #exam[dept,course,room,instructor-id,timeslot-id,no of students]  / #editable=False
    accessCode = models.TextField(default='')  #editable=False
    orgId = models.IntegerField(default=0)   #forign key mn table el accounts(organisations)/one(org) to many(timetables)/one(timetable) to one(org) / editable = False



