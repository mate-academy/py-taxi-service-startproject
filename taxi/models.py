from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=25)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name='cars'
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name="cars"
    )


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)
