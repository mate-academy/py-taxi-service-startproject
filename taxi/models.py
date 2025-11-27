from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models

class Driver(AbstractUser):
    license_number = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return f"{self.username} ({self.license_number})"


class Manufacturer(models.Model):
    name = models.CharField(max_length=50)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    model = models.CharField(max_length=50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    # Використовуємо AUTH_USER_MODEL для зв’язку з водіями
    drivers = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return f"{self.model} - {self.manufacturer.name}"
