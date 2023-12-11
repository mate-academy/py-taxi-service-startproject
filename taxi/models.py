from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings


class Manufacturer(models.Model):
    name = models.CharField(
        max_length=50, unique=True, null=True, blank=True
    )
    country = models.CharField(
        max_length=50, null=True, blank=True
    )

    class Meta:
        verbose_name = 'manufacturer'
        verbose_name_plural = 'manufacturers'

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(
        max_length=50, null=True, blank=True
    )
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE
    )
    drivers = models.ManyToManyField(
        settings.AUTH_USER_MODEL, related_name="cars"
    )

    class Meta:
        verbose_name = 'Car'
        verbose_name_plural = 'Cars'

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(
        max_length=50, unique=True, null=True, blank=True
    )

    class Meta:
        verbose_name = 'driver'
        verbose_name_plural = 'drivers'

    def __str__(self):
        return self.username
