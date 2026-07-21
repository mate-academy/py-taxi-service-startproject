from django.shortcuts import render
from .models import Driver, Manufacturer, Car


def index(request):

    drivers = Driver.objects.all()
    manufacturers = Manufacturer.objects.all()
    return render(
        request,
        "taxi/index.html",
        {
            "page_title": "Home page",
            "drivers": drivers,
            "manufacturers": manufacturers,
            "cars_count": Car.objects.all().count(),
            "drivers_count": Driver.objects.all().count(),
            "manufacturers_count": Manufacturer.objects.all().count(),
        },
    )


def cars(request):
    cars = Car.objects.all()
    return render(request, "taxi/cars.html", {"cars": cars})


def drivers(request):
    drivers = Driver.objects.all()
    return render(request, "taxi/drivers.html", {"drivers": drivers})


def manufacturers(request):
    manufacturers = Manufacturer.objects.all()
    return render(request, "taxi/manufacturers.html", {"manufacturers": manufacturers})
