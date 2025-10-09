from django.db import models
from taxi_service.settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.DO_NOTHING)
    driver = models.ManyToManyField(to=AUTH_USER_MODEL, related_name="cars")
