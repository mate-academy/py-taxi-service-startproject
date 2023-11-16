from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name} {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True, blank=True)

    def __str__(self) -> str:
        return f"{self.username} {self.license_number}"

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
        ordering = ["-date_joined"]


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(to=settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self) -> str:
        return f"Car: {self.model}, {self.manufacturer.name}"
