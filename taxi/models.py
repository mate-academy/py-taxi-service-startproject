from django.contrib.auth.models import AbstractUser
from django.db import models

class Manufacturer(models.Model):
    name = models.CharField(max_length=63, unique=True)
    country = models.CharField(max_length=63)


class Driver(AbstractUser):
    license_number = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=63)
    email = models.CharField(max_length=63)
    password = models.CharField(max_length=63)
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)



    class Meta:
        verbose_name = "Driver"
        verbose_name_plural = "Drivers"



class Car(models.Model):
    model = models.CharField(max_length=30)
    manufacturer = models.ManyToManyField(to=Manufacturer)
    drivers = models.ManyToManyField(to=Driver)
