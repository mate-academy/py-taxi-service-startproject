from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )
    driver = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
