from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=255, unique=True)
    country = models.CharField(max_length=255)


class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
