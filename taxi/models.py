from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=70, unique=True)
    country = models.CharField(max_length=70)

    class Meta:
        ordering = ["name"]

    def __str__(self) -> str:
        return f"{self.name} ({self.country})"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=17, unique=True)

    class Meta:
        ordering = ["username"]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name}) " \
               f"license number: {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=70)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="car_manufacturer",
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="drivers",
    )

    class Meta:
        ordering = ["model"]

    def __str__(self) -> str:
        return self.model
