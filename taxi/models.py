from django.db import models
from django.contrib.auth.models import AbstractUser

class Manufacturer(models.Model):
    name = models.CharField(max_length=55, unique=True)
    country = models.CharField(max_length=55)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=55)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")

    def __str__(self):
        return self.model

class Driver(AbstractUser):
    license_number = models.CharField(max_length=55, unique=True)
    cars = models.ManyToManyField(Car, related_name="drivers")

    def __str__(self):
        return self.username
