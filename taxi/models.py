from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name}"

class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)
    # password = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "Drivers"
        verbose_name = "Driver"






class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver)

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"


