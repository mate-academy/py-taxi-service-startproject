from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        db_table = "Driver"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.OneToOneField(Manufacturer, on_delete=models.CASCADE,
                                        related_name="cars")

    drivers = models.ManyToManyField(Driver, related_name="cars")
