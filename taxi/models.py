from django.contrib.auth.models import AbstractUser
from django.db import models
from taxi_service.settings import AUTH_USER_MODEL


class Driver(AbstractUser):
    license_number = models.CharField(unique=True, max_length=255)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(AUTH_USER_MODEL)

    def __str__(self):
        return f"{self.manufacturer}, {self.model}"
