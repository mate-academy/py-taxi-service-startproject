from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    license_number = models.CharField(max_length=10, unique=True)

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return (f"{self.license_number}: "
                f"({self.first_name} {self.last_name})")


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name}, {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )

    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ("model", "manufacturer", )

    def __str__(self):
        return self.model
