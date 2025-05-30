from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    model = models.CharField(max_length=100)
    drivers = models.ManyToManyField('Driver', related_name='drivers')

    class Meta:
        ordering = ('model',)

    def __str__(self) -> str:
        return self.model
