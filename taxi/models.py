from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=50)
    drivers = models.ManyToManyField(get_user_model(), related_name='cars')
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.CASCADE,
                                     related_name='cars')
