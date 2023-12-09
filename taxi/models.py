from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=50, unique=True)
    country = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name} from {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField("Driver", related_name="cars")
