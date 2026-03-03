from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, unique=True)
    country = models.CharField(max_length=255, null=False, blank=False)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return f"{self.name}, {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=68, unique=True)

    class Meta:
        ordering = ("first_name", "last_name", )

    def __str__(self):
        return (f"Name: {self.first_name}, surname: {self.last_name}, "
                f"license number: {self.license_number}")


class Car(models.Model):
    model = models.CharField(max_length=255, null=False, blank=False)
    manufacturer = models.ForeignKey(
        Manufacturer, related_name="cars", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars", blank=True
    )

    class Meta:
        ordering = ("model", )

    def __str__(self):
        return f"Car model: {self.model}, manufacturer: {self.manufacturer}"
