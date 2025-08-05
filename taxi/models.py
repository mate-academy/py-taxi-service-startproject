from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return  f"{self.name} ({self.country})"

class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=63,
        unique=True,
        null=False,
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name} {self.license_number}"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacture = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="Cars",
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="Cars")

    def __str__(self):
        return f"{self.model} {self.drivers}"
