from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} from {self.country}"


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255)

    class Meta:
        constraints = [
            UniqueConstraint(name='license', fields=['license_number'])
        ]
        verbose_name = 'Driver'
        verbose_name_plural = 'Drivers'

    def __str__(self):
        return self.license_number


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.CASCADE,
    )
    drivers = models.ManyToManyField(
        Driver,
    )

    def __str__(self):
        return self.model
