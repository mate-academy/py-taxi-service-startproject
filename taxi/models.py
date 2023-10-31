from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=60,
        unique=True,
        null=False,
        blank=False
    )
    country = models.CharField(max_length=60, null=False, blank=False)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return f"{self.name}, country: {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=60, null=False, blank=False)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    drivers = models.ManyToManyField(to="Driver", related_name="cars")

    def __str__(self):
        return f"{self.model}, {self.manufacturer.country}"


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=60, null=False, blank=False, unique=True
    )
    username = models.CharField(
        max_length=60,
        null=False,
        blank=False,
        unique=True
    )
    email = models.EmailField(null=False, blank=False)
    password = models.CharField(max_length=60, null=False, blank=False)

    def __str__(self):
        return f"{self.username} {self.license_number}"
