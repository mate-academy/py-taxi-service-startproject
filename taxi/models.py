from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ("name", )

    def __str__(self):
        return f"{self.name} country: {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ("manufacturer", )

    def __str__(self):
        return f"model: {self.model}, manufacturer: "


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ("username", )

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"