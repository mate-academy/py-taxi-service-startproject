from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        pass


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)

    class Meta:
        pass


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    driver = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="drivers")

    def __str__(self):
        return self.model

    class Meta:
        pass
