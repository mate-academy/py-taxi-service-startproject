from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", "country")

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=150, unique=True)

    class Meta:
        ordering = ("first_name", "last_name",)

    def __str__(self):
        return f"{self.username}: {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=150)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="cars", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars",
    )

    class Meta:
        ordering = ("model", "manufacturer",)

    def __str__(self):
        return self.model
