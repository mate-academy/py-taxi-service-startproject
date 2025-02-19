from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from taxi_service.settings import AUTH_USER_MODEL


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ["country", "name"]

    def __str__(self):
        return f"{self.name} {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )

    class Meta:
        ordering = ["model"]

    def __str__(self):
        return f"{self.manufacturer} {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.username}, {self.license_number}"
