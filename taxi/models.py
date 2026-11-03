from django.contrib.auth.models import AbstractUser
from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(unique=True)
    country = models.CharField()


class Driver(AbstractUser):
    licence_number = models.CharField(unique=True)
    username = models.CharField()
    email = models.CharField()
    password = models.CharField()
    first_name = models.CharField()
    last_name = models.CharField()


class Car(models.Model):
    model = models.CharField()
    manufacturer = models.ForeignKey(Manufacturer)
    drivers = models.ManyToManyField(Driver)