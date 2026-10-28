from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    drivers = models.ManyToManyField("Driver", related_name="cars")

    class Meta:
        verbose_name = "car"
        verbose_name_plural = "cars"
    

class Driver(AbstractUser):
    license_number= models.CharField(max_length=255, unique=True)
