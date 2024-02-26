from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(to=Manufacturer,
                                     on_delete=models.CASCADE,
                                     related_name="cars")
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars")

    def __str__(self):
        return f"{self.manufacturer}, Model: '{self.model}'"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        verbose_name = "Driver"

        constraints = [
            (UniqueConstraint(fields=["license_number"],
                              name="unique_license_number"))
        ]
