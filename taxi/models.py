from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


# Driver (license_number: unique, username, email, password, first_name, last_name)
class Driver(AbstractUser):
    license_number = models.CharField(max_length=65, unique=True)

    def __str__(self):
        return self.username


# Manufacture (name: unique, country)
class Manufacture(models.Model):
    name = models.CharField(max_length=65, unique=True)
    country = models.CharField(max_length=65)

    def __str__(self):
        return self.name

# Car (model, manufacture, drivers)
class Car(models.Model):
    model = models.CharField(max_length=65)
    manufacturer = models.ForeignKey(
        Manufacture, on_delete=models.CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    def __str__(self):
        return self.model
