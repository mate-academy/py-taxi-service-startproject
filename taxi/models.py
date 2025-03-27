from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(
        to=Manufacturer,
        on_delete=CASCADE,
        related_name="cars"
    )
    drivers = models.ManyToManyField(
        to="Driver",
        related_name="cars"
    )


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
