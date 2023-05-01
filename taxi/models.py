from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Driver(AbstractUser):
    license_number = models.CharField(max_length=10)

    class Meta:
        constraints = [
            UniqueConstraint(fields=["license_number"], name="unique_driver_license_number")
        ]
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self) -> str:
        return f"{self.username} ({self.first_name} {self.last_name})"


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return f"{self.model} {self.manufacturer}"
