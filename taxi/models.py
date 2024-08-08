from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.CharField(max_length=100)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=100, unique=True)


class Car(models.Model):
    model = models.CharField(max_length=100)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    driver = models.ManyToManyField(Driver)
