from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .forms import ContactForm, FlightForm
from .models import Flight
from datetime import datetime


# Create your views here.
def index(request):
    flights = Flight.objects.filter(date_lte=datetime.now().date())
    context = {'flight_list': flights, 'app_name': 'FlightApp'}
    return render(request, 'index.html', context)


def details(request, flight_id):
    flight = Flight.objects.filter(id=flight_id).first()
    context = {'flight_data': flight, 'app_name': 'FlightApp'}
    return render(request, 'details.html', context)


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            pass
        return redirect('index')

    form = ContactForm()
    context = {'form': form}
    return render(request, 'contact.html', context)


def add_flight(request):
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('index')

    form = FlightForm()
    context = {'form': form}
    return render(request, 'add_flight.html', context)

def edit_flight(request, flight_id):
    flight = get_object_or_404(Flight, pk=flight_id)
    if request.method == 'POST':
        form = FlightForm(request.POST, request.FILES, instance=flight)
        if form.is_valid():
            form.save()

        return redirect('index')
    form = FlightForm(instance=flight)
    context = {'form': form}
    return render(request, 'edit_flight.html', context)