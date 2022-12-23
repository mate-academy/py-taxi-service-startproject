from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"
        ordering = ["username"]


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    class Meta:
        ordering = ['manufacturer']
