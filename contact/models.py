from django.db import models


class Contact(models.Model):
    FirstName = models.CharField(max_length=255)
    LastName = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    TelephoneNumber = models.IntegerField()
    Country = models.CharField(max_length=255)
    Message = models.TextField()

    def __str__(self):
        return self.FirstName+self.LastName

