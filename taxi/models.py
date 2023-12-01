from typing import List

from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} - {self.country}"

    class Meta:
        pass


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    # username
    # email
    # password
    # first_name
    # last_name
    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name}). License number: {self.license_number}"

    class Meta:
        pass


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="manufacturer", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        Driver, related_name="drivers", blank=True,
    )

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

    class Meta:
        pass
