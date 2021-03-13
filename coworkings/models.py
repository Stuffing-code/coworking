from django.db import models
from datetime import *

# Create your models here.
class NumberOffice(models.Model):
    number_office = models.CharField(max_length=30)

    def __str__(self):
        return self.number_office


class Reservation(models.Model):
    number_office = models.ForeignKey(NumberOffice, on_delete=models.CASCADE)
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()

    def __str__(self):
        date_create = f'from:{self.datetime_from.isoformat()} \
        to: {self.datetime_to.isoformat()}'
        return date_create
