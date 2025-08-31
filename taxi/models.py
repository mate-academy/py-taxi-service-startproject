from django.db import models
from django.contrib.auth.models import AbstractUser
from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    country = models.CharField()

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(unique=True,
                                      null=True)

    def __str__(self) -> str:
        return self.username


class Car(models.Model):
    model = models.CharField()
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='cars')

    def __str__(self) -> str:
        return self.model
