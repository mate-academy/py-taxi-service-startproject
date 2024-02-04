from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63)
    country = models.CharField(max_length=63)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["name"],
                name="unique_name"
            )
        ]

    def __str__(self):
        return f"{self.name}"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["license_number"],
                name="unique_license_number"
            )
        ]

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"

