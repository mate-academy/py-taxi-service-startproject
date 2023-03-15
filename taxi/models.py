from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} {self.first_name} {self.last_name}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name}, {self.country}"


class Car(models.Model):
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    model = models.CharField(max_length=63)
    driver = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.model}  ({self.manufacturer})"
