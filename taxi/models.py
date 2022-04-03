from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import UniqueConstraint

from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=56)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'


class Car(models.Model):
    model = models.CharField(max_length=56)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='cars')

    class Meta:
        ordering = ['manufacturer', 'model']

    def __str__(self):
        return f'{self.manufacturer} {self.model}'


class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, primary_key=True)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=["license_number"],
                name='license_number'
            )
        ]

        verbose_name_plural = 'drivers'
        verbose_name = 'driver'
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f"{self.license_number} | {self.first_name} {self.last_name} | '{self.username}'"
