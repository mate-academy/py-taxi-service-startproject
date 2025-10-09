from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=100)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=models.DO_NOTHING)
    driver = models.ManyToManyField(to=Driver, related_name="cars")
