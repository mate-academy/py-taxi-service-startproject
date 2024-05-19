from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=256)
    manufacturer = models.ForeignKey(to=Manufacturer,
                                     on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars"
)

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.username
