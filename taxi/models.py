from django.contrib.auth.models import AbstractUser
from django.db import models
from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    county = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} from {self.county}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(AUTH_USER_MODEL)

    def __str__(self) -> str:
        return f"{self.model} by {self.manufacturer}"
