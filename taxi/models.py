from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.username

class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars")

    def __str__(self):
        return self.model