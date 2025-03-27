from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"""{self.username}: (
            {self.first_name},
            {self.last_name},
            {self.license_number})"""


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="manufactured_cars")
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="driven_cars")

    def __str__(self):
        return self.model
