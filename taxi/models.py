from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    def __str__(self) -> str:
        full_name = self.get_full_name()
        if full_name:
            return f"{self.get_username()} - {self.get_full_name()}"
        return self.get_username()


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        default_related_name = "cars"

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
