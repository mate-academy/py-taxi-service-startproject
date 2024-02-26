from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    model = models.TextField()
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")


class Manufacturer(models.Model):
    name = models.TextField(unique=True)
    country = models.TextField()

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.TextField(unique=True)


