from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Car(models.Model):
    model = models.CharField(max_length=255)
    manufacturer = models.ForeignKey("Manufacturer", on_delete=models.CASCADE,
                                     related_name='cars')
    drivers = models.ManyToManyField("Driver", related_name="cars")

    def __str__(self):
        return self.model

class Driver(AbstractUser):
    username = models.CharField(max_length=150, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    license_number = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.username

class Manufacturer(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name