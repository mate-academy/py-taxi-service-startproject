from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        to=settings.AUTH_USER_MODEL, related_name="cars"
    )

    def __str__(self):
        return f"{self.model}"
