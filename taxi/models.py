from django.conf import settings
from django.conf.global_settings import AUTH_USER_MODEL
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import ManyToManyField


class Manufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=200)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ("model",)

    def __str__(self):
        return f"{self.manufacturer} {self.model}"

class Driver(AbstractUser):
    license_number = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ("username",)

    def __str__(self):
        return f"{self.username}: ({self.first_name} {self.last_name})"
