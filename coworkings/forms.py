from django import forms
from django.forms.widgets import DateTimeInput

from .models import Reservation, NumberOffice


class NewReservationsOfficesForm(forms.ModelForm):
    class Meta:
        model = Reservation
        datetime = ['%Y-%m-%d %H:%M:%S']
        fields = ['number_office', 'datetime_from', 'datetime_to']
        datetime_from =  forms.DateField(widget=DateTimeInput(format=datetime))
        datetime_to = forms.DateField(widget=DateTimeInput(format=datetime))
        lables = {'Office': '', 'datetime_from': datetime_from, 'datetime_to': datetime_to}
