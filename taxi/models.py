from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return str(self.name)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    class Meta:
        ordering = ['username']


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars")

    class Meta:
        ordering = ['model']

    def __str__(self) -> str:
        return f"{self.manufacturer} {self.model}"
