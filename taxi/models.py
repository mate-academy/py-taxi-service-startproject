from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    is_staff = models.BooleanField(default=False)
