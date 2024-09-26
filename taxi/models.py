from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def str(self):
        return self.name


class Driver(AbstractUser):
    license_number = models.CharField(max_length=15, unique=True)
    groups = models.ManyToManyField(Group, related_name="driver_related")
    user_permissions = models.ManyToManyField(Permission, related_name="driver_related")

    class Meta:
        verbose_name = "driver"
        verbose_name_plural = "drivers"


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="cars"
    )

    def str(self):
        return f"{self.manufacturer.name}: {self.model}"
