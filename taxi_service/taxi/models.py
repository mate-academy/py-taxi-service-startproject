from django.db import models
from django.contrib.auth.models import AbstractUser
from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Driver(AbstractUser):
    licence_number = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
