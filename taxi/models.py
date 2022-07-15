from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(unique=True, max_length=255)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f"{self.name}: {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer,
                                     on_delete=models.CASCADE,
                                     related_name='cars')
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name='cars')

    class Meta:
        ordering = ['model']

    def __str__(self):
        return f"{self.model}: {self.manufacturer}"


class Driver(AbstractUser):
    license_number = models.CharField(unique=True, max_length=255)

    class Meta:
        ordering = ['last_name']
        verbose_name = 'driver'
        verbose_name_plural = 'drivers'

    def __str__(self):
        return f"{self.username}: {self.first_name} {self.last_name}"
