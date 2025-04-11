from django.db import models
from django.contrib.auth.models import AbstractUser

class Driver(AbstractUser):
    license_number = models.CharField(max_length=15, unique=True)

class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)

class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
