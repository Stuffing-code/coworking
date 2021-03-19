from django.db import models
from datetime import *

# Create your models here.
class NumberOffice(models.Model):
    number_office = models.CharField(max_length=40)

    def __str__(self):
        return self.number_office

    def __iter__(self):
        return iter(self.number_office)


class Reservation(models.Model):
    number_office = models.ForeignKey(
        NumberOffice,
        on_delete=models.CASCADE,
        unique_for_date="datetime_from",
    )
    datetime_from = models.DateTimeField()
    datetime_to = models.DateTimeField()


    def __str__(self):
        date_create = f'{self.number_office} Reserved: {self.datetime_from} to {self.datetime_to}'
        return date_create

    def __iter__(self):
        return iter(self.number_office)