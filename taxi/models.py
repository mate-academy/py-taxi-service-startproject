from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        to=Manufacturer, on_delete=models.CASCADE  # related_name="cars"
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL,
        # related_name="cars"
    )

    def __str__(self):
        return f"{self.drivers}:{self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ("license_number", )

    def __str__(self):
        return f"{self.first_name} {self.last_name} : {self.license_number}"
