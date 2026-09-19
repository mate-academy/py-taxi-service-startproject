from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Car, Driver, Manufacturer


def index(request):
    return render(request, "taxi/index.html")


class CarListView(generic.ListView):
    model = Car


class CarDetailView(generic.DetailView):
    model = Car


class CarCreateView(generic.CreateView):
    model = Car
    fields = ["model", "manufacturer", "drivers"]
    success_url = reverse_lazy("car-list")


class CarUpdateView(generic.UpdateView):
    model = Car
    fields = ["model", "manufacturer", "drivers"]
    success_url = reverse_lazy("car-list")


class CarDeleteView(generic.DeleteView):
    model = Car
    success_url = reverse_lazy("car-list")


class DriverListView(generic.ListView):
    model = Driver


class DriverDetailView(generic.DetailView):
    model = Driver


class DriverCreateView(generic.CreateView):
    model = Driver
    fields = ["username", "first_name", "last_name", "license_number"]
    success_url = reverse_lazy("driver-list")


class DriverUpdateView(generic.UpdateView):
    model = Driver
    fields = ["username", "first_name", "last_name", "license_number"]
    success_url = reverse_lazy("driver-list")


class DriverDeleteView(generic.DeleteView):
    model = Driver
    success_url = reverse_lazy("driver-list")


class ManufacturerListView(generic.ListView):
    model = Manufacturer


class ManufacturerDetailView(generic.DetailView):
    model = Manufacturer


class ManufacturerCreateView(generic.CreateView):
    model = Manufacturer
    fields = ["name", "country"]
    success_url = reverse_lazy("manufacturer-list")


class ManufacturerUpdateView(generic.UpdateView):
    model = Manufacturer
    fields = ["name", "country"]
    success_url = reverse_lazy("manufacturer-list")


class ManufacturerDeleteView(generic.DeleteView):
    model = Manufacturer
    success_url = reverse_lazy("manufacturer-list")
