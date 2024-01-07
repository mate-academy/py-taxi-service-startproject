from django.contrib.auth.models import AbstractUser
from django.db import models
from taxi_service import settings

# Create your models here.


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}, {self.country}"


class Car(models.Model):
    model = models.CharField(max_length=255, unique=True)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="manufacturer"
    )
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL)

    def __str__(self) -> str:
        return f"{self.model} {self.manufacturer} {','.join([driver.full_name for driver in self.drivers.all()])}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)

    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self) -> str:
        return (
            f"{self.license_number} {self.username} {self.email} {self.password} "
            f"{self.first_name} {self.last_name}"
        )
