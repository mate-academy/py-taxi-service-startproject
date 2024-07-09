from django.contrib.auth.models import AbstractUser

from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    class Meta:
        ordering = ("license_number",)

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(Driver)

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return f"{self.model} by {self.manufacturer.name}"
