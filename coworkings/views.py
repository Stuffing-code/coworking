from django.shortcuts import render, redirect

from .models import NumberOffice, Reservation
from .forms import NewReservationsOfficesForm
# Create your views here.

def index(request):
    """Home page"""
    office = NumberOffice.objects.all()
    context = {'office': office}
    return render(request, 'coworkings/index.html', context)

def reservs(request):
    """Page new reservations office."""
    if request.method == 'POST':
        # create a form
        form = NewReservationsOfficesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('coworkings:index')
    else:
        form = NewReservationsOfficesForm()

    context = {"form": form}
    return render(request, 'coworkings/reservs.html', context)

def place(request, place_id):
    """Show reserved office time"""
    office_reserv_time = NumberOffice.objects.get(id=place_id)
    reservs = office_reserv_time.reservation_set.order_by('id')

    context = {"office_reserv_time": office_reserv_time, 'reservs': reservs}
    return render(request, 'coworkings/place_reserv.html', context)

def look_at_vacant_offices(request):
    """Page for look vacant offices"""
    if request.GET:
        offices = NumberOffice.objects.all()
        reservations = Reservation.objects.all()
        post_from = request.GET['datetime_from']
        post_to = request.GET['datetime_to']
        filteroffice = reservations.all().filter(
            datetime_from__gte=post_from, datetime_to__lte=post_to
            )
        # print(type(filteroffice))
        reservednumberoffice = set()
        #  set reserved office for corect time
        for i in filteroffice:
            reservednumberoffice.add(i.number_office)
        print(reservednumberoffice)
        
        context = {'offices': offices, "reservednumberoffice": reservednumberoffice}

        return render(request, 'coworkings/vacant_offices.html', context)
    else:
        return render(request, 'coworkings/look_at_vacant_offices.html')
