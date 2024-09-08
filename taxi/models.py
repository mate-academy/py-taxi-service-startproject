from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.PROTECT, related_name="cars"
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="driven_cars"
    )

    class Meta:
        ordering = ("model",)

    def __str__(self) -> str:
        return f"{self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ("license_number",)
