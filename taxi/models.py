from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Car(models.Model):
    model = models.TextField()
    manufacturer = models.ForeignKey(
        "Manufacturer", on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Manufacturer(models.Model):
    name = models.TextField(unique=True)
    country = models.TextField()

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.TextField(unique=True)
    password = models.TextField()

