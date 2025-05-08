from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    street = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100, blank=True, null=True)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cars')

    def __str__(self):
        return f"{self.manufacturer.name} {self.model}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
