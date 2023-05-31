from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.SET_NULL, null=True, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"
