from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=80, unique=True)
    country = models.CharField(max_length=80)

    def __str__(self) -> str:
        return f"{self.name}: {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ("username",)


class Car(models.Model):
    model = models.CharField(max_length=95, unique=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ("model",)
