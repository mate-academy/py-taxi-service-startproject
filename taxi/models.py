from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Driver(AbstractUser):
    license_number = models.CharField(max_length=120 , unique=True)

    def __str__(self):
        return f"{self.username}, license number: {self.license_number}"

    class Meta:
        verbose_name_plural = 'Drivers'
        verbose_name = 'Driver'
        ordering = ['username']


class Car(models.Model):
    model = models.CharField(max_length=120)
    manufacturer = models.ForeignKey(
        Manufacturer,
        related_name='cars',
        on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL,
        related_name='cars',
    )
