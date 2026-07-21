from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import CASCADE

from taxi_service import settings


class Driver(AbstractUser):
    license_number = models.CharField(max_length=63, unique=True)

    class Meta:
        ordering = ("license_number",)
        verbose_name = "driver"
        verbose_name_plural = "drivers"

    def __str__(self):
        return f"{self.first_name} {self.last_name}" f" - license-{self.license_number}"


class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63, null=True, blank=True)

    class Meta:
        ordering = ("name",)
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self):
        return f"{self.name} - {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=63)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=CASCADE, related_name="cars"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="cars")

    class Meta:
        ordering = ("model",)
        verbose_name = "car"
        verbose_name_plural = "cars"

    def __str__(self):
        drivers = "; ".join(str(driver) for driver in self.drivers.all())
        return (
            f"{self.model},"
            f" manufactured by - {self.manufacturer},"
            f" drivers - {drivers}"
        )
