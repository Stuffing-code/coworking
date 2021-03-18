from django.db import models
from datetime import *

# Create your models here.
class NumberOffice(models.Model):
    number_office = models.CharField(max_length=40)

    def __str__(self):
        return self.number_office

    def check_time(self):
        pass


class Reservation(models.Model):
    number_office = models.ForeignKey(NumberOffice, on_delete=models.CASCADE)
    datetime_from = models.DateTimeField(unique=True)
    datetime_to = models.DateTimeField(unique=True)


    def __str__(self):
        date_create = f'{self.number_office} Reserved: {self.datetime_from.isoformat()} to {self.datetime_to.isoformat()}'
        return date_create
