from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=64, unique=True)
    country = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=64, unique=True)
    username = models.CharField(max_length=64, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=256)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"


class Car(models.Model):
    model = models.CharField(max_length=64)
    manufacturer = models.OneToOneField(Manufacturer, unique=True, on_delete=models.CASCADE)
    drivers = list[models.ManyToManyField(Driver, related_name='cars')]

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
