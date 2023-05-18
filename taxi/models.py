from django.db import models
from django.contrib.auth.models import AbstractUser


class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE)
    drivers = models.ManyToManyField("Driver")

    def __str__(self) -> str:
        return self.model
    
class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)
    
    class Meta:
        verbose_name ="Driver"
        verbose_name_plural ="Drivers"
    
