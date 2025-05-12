from django.shortcuts import render
from django.http import HttpResponse
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