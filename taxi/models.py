from django.contrib.auth.models import AbstractUser
from django.db import models

from taxi_service import settings


class Manufacturer(models.Model):
    name = models.CharField(max_length=200, unique=True)
    country = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} : {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["username"]
        verbose_name_plural = "drivers"
        verbose_name = "driver"

    def __str__(self):
        return f"{self.first_name} {self.last_name}" \
               f" ({self.username} : {self.license_number})"


class Car(models.Model):
    model = models.CharField(max_length=200)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                     related_name="cars")

    def __str__(self):
        return f"{self.model}," \
               f" drivers : {list(self.drivers.all().values_list('username'))}"
