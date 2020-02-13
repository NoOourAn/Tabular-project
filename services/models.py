from django.db import models

# Create your models here.
class Timetables(models.Model):
    day = models.DateField
    startTime = models.TimeField
    dueTime = models.TimeField
    exam = models.TextField
    room = models.TextField
    accessCode = models.TextField
    orgId = models.IntegerField     #forign key mn table el accounts(organisations)/one(org) to many(timetables)/one(timetable) to one(org)

