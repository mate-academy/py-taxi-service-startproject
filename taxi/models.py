from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


class Manufacturer(models.Model):
    name = models.TextField()
    country = models.TextField()

    def __str__(self):
        return f"{self.name} from {self.country}"


class Car(models.Model):
    model = models.TextField()
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.model


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)
    cars = models.ManyToManyField(
        Car,
    )

    class Meta:
        constraints = [
            UniqueConstraint(name='license', fields=['license_number'])
        ]
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.license_number
