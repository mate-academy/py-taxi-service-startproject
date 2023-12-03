from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"name: {self.name} country: {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        ordering = ["username"]
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    def __str__(self):
        return f"{self.username} ({self.first_name}" \
               f" {self.last_name}| licence: {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=255, blank=True)
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
        ordering = ["model"]

    def __str__(self):
        return f" model: {self.model} manufacturer: {self.manufacturer.name}"
