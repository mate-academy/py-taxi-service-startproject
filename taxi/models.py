from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    def __str__(self):
        return f"{self.name} {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return f"Name: {self.model}. Manufacturer: {self.manufacturer}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["license_number"],
                name="unique_license_number"
            )
        ]
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"
