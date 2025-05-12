from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from taxi_service.settings import AUTH_USER_MODEL


class Manufacturer(models.Model):
    name = models.CharField(max_length=254)
    country = models.CharField(max_length=254)

    def __str__(self):
        return self.name
    


class Driver(AbstractUser):
    license_number = models.CharField(unique=True, max_length=254)

    class Meta:
        ordering = ("username", )

class Car(models.Model):
    model = models.CharField(max_length=254)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars",
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ("model", )

    def __str__(self):
        return f"Model: {self.model}; manufacturer: {self.manufacturer.name}"
