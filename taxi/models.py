from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField()

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"


class Manufacturer(models.Model):
    name = models.CharField()
    country = models.CharField()

    def __str__(self):
        return f"{self.name} ({self.country})"


class Car(models.Model):
    model = models.CharField()
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name="cars",
        on_delete=models.CASCADE,
        blank=True,
    )
    driver = models.ManyToManyField(Driver, related_name="cars", blank=True)

    def __str__(self):
        return self.model
