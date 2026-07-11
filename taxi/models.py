from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    country = models.CharField()

    def __str__(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(unique=True)
    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return self.username


class Car(models.Model):
    model = models.CharField()
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self):
        return self.model
