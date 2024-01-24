from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=30, unique=True)
    country = models.CharField(max_length=30)

    class Meta:
        ordering = ["country"]

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=30)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    def __str__(self):
        return (f"{self.manufacturer} {self.model}"
                f"({self.manufacturer.country})")
