from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    # username = models.CharField(max_length=255)
    # email = models.CharField(max_length=255)
    # password = models.CharField(max_length=255)
    # first_name = models.CharField(max_length=255)
    # last_name = models.CharField(max_length=255)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="manufacturer"
    )
    drivers = models.ManyToManyField(
        Driver, related_name="drivers"
    )
