from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True, null=True)

    class Meta():
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"




class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"

