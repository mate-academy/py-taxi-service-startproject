from django.shortcuts import render
from django.http import HttpResponse
from .models import Driver, Car, Manufacturer


def taxi_view(request):
    return HttpResponse("Ласкаво просимо до Taxi Service!")
# Create your views here.

def table_view(request):
    drivers = Driver.objects.all()
    cars = Car.objects.all()
    manufacturers = Manufacturer.objects.all()
    return render(request, 'taxi/table_view.html', {
        'drivers': drivers,
        'cars': cars,
        'manufacturers': manufacturers
    })
