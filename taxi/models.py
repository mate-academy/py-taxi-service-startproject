from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.TextField(unique=True)
    country = models.TextField()

    def __str__(self) -> str:
        return f"{self.name}"


class Driver(AbstractUser):
    license_number = models.TextField(unique=True)

    def __str__(self) -> str:
        return f"{self.username}"


class Car(models.Model):
    model = models.TextField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver)

    def __str__(self) -> str:
        return f"{self.model}"
