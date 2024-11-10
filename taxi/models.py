from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ForeignKey

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver, related_name="cars")

    def __str__(self):
        return f"{self.manufacturer} {self.model}"
