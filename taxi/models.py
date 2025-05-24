from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return f"{self.name} - {self.country}"


class Driver(AbstractUser):
    # inherit all fields from AbstractUser
    license_number = models.CharField(max_length=255)

    class Meta:
        ordering = ['username']
        constraints = [
            models.UniqueConstraint(fields=['license_number'], name='unique_licence')
        ]

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"

class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE, related_name="cars")
    drivers = models.ManyToManyField(get_user_model(), related_name="cars")

    class Meta:
        ordering = ['model']

    def __str__(self) -> str:
        return f"{self.manufacturer} - {self.model}"
