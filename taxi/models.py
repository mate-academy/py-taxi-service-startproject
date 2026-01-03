from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings



class Manufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
        related_name="cars"
    )
    model = models.CharField(max_length=200)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)



class Driver(AbstractUser):
    license_number = models.CharField(max_length=200, unique=True)