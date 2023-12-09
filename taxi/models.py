from django.db import models
from django.contrib.auth.models import AbstractUser

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} from {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name} ({self.username})"


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return f"{self.manufacturer.name} {self.model}"
