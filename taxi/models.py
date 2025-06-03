from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CharField

from taxi_service import settings


# Create your models here.

class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(to="Manufacturer",
                                     on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars")


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self) -> CharField:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'
