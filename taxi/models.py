from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=255)
    country = models.CharField(max_length=255)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        "Driver", related_name="cars"
    )

    class Meta:
        ordering = ["manufacturer"]


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self) -> str:
        return self.username
