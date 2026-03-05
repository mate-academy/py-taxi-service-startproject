from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

class Driver(AbstractUser):
    license_number = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"

class Manufacturer(models.Model):
    name = models.CharField(max_length=20, unique=True)
    country = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Car(models.Model):
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    model = models.CharField(max_length=20)

    def __str__(self):
        return self.model

