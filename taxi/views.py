from django.shortcuts import render
from taxi.models import Car

def car_list(request):
    cars = Car.objects.all()
    return render(request, "taxi/car_list.html", {"cars": cars})
