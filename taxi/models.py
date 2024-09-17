from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"driver {self.username}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    model = models.CharField(max_length=255, unique=True)
    manufacturer = models.ForeignKey(to=Manufacturer,
                                     on_delete=models.CASCADE,
                                     related_name="cars")
    drivers = models.ManyToManyField(to=Driver)
