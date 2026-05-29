from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.name

    country = models.CharField(max_length=63)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    driver = models.ManyToManyField(Driver, related_name="cars")
